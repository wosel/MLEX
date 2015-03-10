import matplotlib.pyplot as plt
from ConfigParser import ConfigParser
import numpy as np
import sys
import getopt

import scipy.optimize as opt
from scipy.stats import norm

__author__ = 'Jakub Hajic'

def gaussCurve(x, mu, sigma, alpha):
    """
    Calculates value at point x of a (scaled) gaussian curve
    ATTN: the resulting curve is not necessarily a distribution, does not integrate to 1 - hence the scaling parameter alpha.

    :param x: where to calculate the value
    :param mu: mean of gaussian
    :param sigma: std dev. of gaussian
    :param alpha: scaling constant
    :return:
    """

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
        :param classNames: labels for the legend in the plot. Python dict indexed by classList
        :param removeNans: should rows (data examples) where the feature is a Numpy NaN be removed?
        :param sigmaWidth: for how many multiples of sigma should the gaussian be plotted on each side of mu

    """
    colorArray =  ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black', 'orange']
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




def main():

    fileName = ''
    configFile = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hf:c:', ['help', 'file=', 'configfile='])
    except getopt.GetoptError:
        print 'plotter.py -f <inputfile> -c <configfile>'
        return 1
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'plotter.py -f <inputfile> -c <configfile>'
        elif opt in('-f', '--file'):
            fileName = arg
        elif opt in ('-c', '--configfile'):
            configFile = arg
    if (fileName == '' or configFile == ''):
        print 'plotter.py -f <inputfile> -c <configfile>'
        return 1

    data = np.loadtxt(fileName)
    parser = ConfigParser()
    parser.readfp(open(configFile))

    plotFeatureValuesAsHistogram(dataSet=data,
                                 featureColID=parser.getint('plot specs', 'featurecol'),
                                 classColID=parser.getint('plot specs', 'classcol'),
                                 classList=[int(x) for x in parser.get('plot specs', 'classids').split(',')],
                                 classNames=dict(zip([int(x) for x in parser.get('plot specs', 'classids').split(',')],parser.get('plot specs', 'classnames').split(','))),
                                 removeNans=parser.getboolean('plot specs', 'removenans'))
    return 0

if __name__ == "__main__":
    sys.exit(main())
