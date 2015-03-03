import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

import scipy.optimize as opt
from scipy.stats import norm

__author__ = 'Jakub Hajic'

def gaussCurve(x, mu, sigma, alpha):
    return alpha * np.exp((-0.5) * (x - mu) * (x - mu) / (sigma * sigma))


def plotFeatureValuesAsHistogram(dataSet, featureColID, classColID, classList=[], classNames = {}, removeNans=True):
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

    """
    colorArray =  ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black', 'orange']
    fig, ax = plt.subplots()
    for classID in classList:
        dataFilteredByClass = dataSet[dataSet[:, classColID] == classID]
        if removeNans:
            dataFilteredByClass = dataFilteredByClass[~np.isnan(dataFilteredByClass[:, featureColID])]
        dataToPlot = dataFilteredByClass[:, featureColID]
        plotSingleClassOverview(data=dataToPlot, color=colorArray[classList.index(classID)], className=str(classNames[classID]))
    legeend = plt.legend(shadow=True)
    plt.show()

def plotSingleClassOverview(data, color, sigmaWidth=6, className=''):
    """
    plots the histograms of a 1D dataset and fits the histogram with a Gaussian

    :param data: the 1D dataset
    :param color: what color should the plot be
    :param sigmaWidth: how many multiples of sigma
    :param className: name of the class for the plot legend
    """

    stats = dict((i, data.tolist().count(i)) for i in set(data))
    guessMu, guessSigma = norm.fit(data)
    guessAlpha = len(data) / (len(stats.keys()) + 1.0)
    [mu, sigma, alpha], cov = opt.curve_fit(gaussCurve, stats.keys(), stats.values(), p0=[guessMu, guessSigma, guessAlpha])
    plt.plot(
        [x for x in range(int(mu - sigmaWidth * sigma), int(mu + sigmaWidth * sigma))],
        [gaussCurve(x, mu, sigma, alpha) for x in
            range(int(mu - sigmaWidth * sigma), int(mu + sigmaWidth * sigma))],
        color=color,
        label=className
    )



    print 'Mu: ' + str(mu) + ' vs ' + str(guessMu)
    print 'Sigma: ' + str(sigma) + ' vs ' + str(guessSigma)
    print 'Alpha: ' + str(alpha) + ' vs ' + str(guessAlpha)
    plt.hist(data, len(stats), color=color)



dataPAMAP = np.loadtxt('subject101.dat')
plotFeatureValuesAsHistogram(dataSet=dataPAMAP, featureColID=2, classColID=1, classList=[1, 3, 5], classNames = {1:'Lying', 3:'Standning', 5:'Running'}, removeNans=True)
