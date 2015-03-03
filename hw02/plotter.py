import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

import scipy.optimize as opt
from scipy.stats import norm

__author__ = 'Jakub Hajic'

def gaussCurve(x, mu, sigma, alpha):
    return alpha * np.exp((-0.5) * (x - mu) * (x - mu) / (sigma * sigma))


def plotFeatureValuesAsHistogram(dataSet, featureColID, classColID, classList=[], classNames = {}, removeNans=True, sigmaWidth=6):
    """
        Function designed to overview distribution of feature values within given classes
        From a dataset, specify one column as the feature and one as the class. This function will plot a histogram
            of the values for each class, and fit a gaussian using least-square optimization (scipy.curve_fit)

        :param dataSet: your dataset expects dataSet to be a numpy 2D matrix w/ row ~ data example, col ~ feature/class
        :param featureColID: which column is the desired feature in. Indexed from 0
        :param classColID: which column is the class designator in. Indexed from 0
        :param classList: list of classes to display the feature value histogram for (use values fouond in the dataset)
        :param classNames: labels for the legend in the plot. Dictionary indexed by classList
        :param removeNans: should rows (data examples) where the feature is a Numpy NaN be removed?
        :param sigmaWidth: for how many multiples of sigma should the gaussian be plotted on each side of mu

    """
    colorArray =  ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black', 'orange']
    fig, ax = plt.subplots()
    for classID in classList:


        #data cleaning
        dataFilteredByClass = dataSet[dataSet[:, classColID] == classID]
        if removeNans:
            dataFilteredByClass = dataFilteredByClass[~np.isnan(dataFilteredByClass[:, featureColID])]
        dataToPlot = dataFilteredByClass[:, featureColID]

        #gaussian fit
        mu, sigma, alpha = fitGaussian(dataToPlot)

        #plotting
        color=colorArray[classList.index(classID)]
        plt.plot(
            [x for x in range(int(mu - sigmaWidth * sigma), int(mu + sigmaWidth * sigma))],
            [gaussCurve(x, mu, sigma, alpha) for x in
                range(int(mu - sigmaWidth * sigma), int(mu + sigmaWidth * sigma))],
            color=color,
            label=str(classNames[classID])
        )
        plt.hist(dataToPlot, len(set(dataToPlot)), color=color)

    legend = plt.legend(shadow=True)
    plt.show()



def fitGaussian(data):
    """
    fits a Gaussian curve (alpha * exp(-(0.5)(x-mu)^2/sigma^2)) through the given data using least-square optimization
        (scipy.optimize.curve_fit)
    :param data: 1D array to fit the 1D gaussian to
    :return: the parameters of the fitted gaussian
    """

    stats = dict((i, data.tolist().count(i)) for i in set(data))
    guessMu, guessSigma = norm.fit(data)
    guessAlpha = len(data) / (len(stats.keys()) + 1.0)
    [mu, sigma, alpha], cov = opt.curve_fit(gaussCurve, stats.keys(), stats.values(), p0=[guessMu, guessSigma, guessAlpha])
    return mu, sigma, alpha



dataPAMAP = np.loadtxt('subject101.dat')
plotFeatureValuesAsHistogram(dataSet=dataPAMAP, featureColID=2, classColID=1, classList=[1, 3, 5], classNames = {1:'Lying', 3:'Standning', 5:'Running'}, removeNans=True)
