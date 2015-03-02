import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

import scipy.optimize as opt
from scipy.stats import norm

__author__ = 'Jakub Hajic'

data = np.loadtxt('subject101.dat')


def gauss(x, mu, sigma, alpha):
    return alpha * np.exp((-0.5) * (x - mu) * (x - mu) / (sigma * sigma))


def plotDataClassOverview(dataList, sigmaWidth=6):
    """
    plots the histograms of multiple 1D-datasets and fits the histograms with a Gaussian

    :param dataList: list of 1D lists of measured data
    :param sigmaWidth: how many multiples of sigma s
    """

    colorArray =  ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black', 'orange']

    #maxStatsLen = 0
    classID = 0
    for data in dataList:
        stats = dict((i, data.tolist().count(i)) for i in set(data))
        guessMu, guessSigma = norm.fit(data)
        guessAlpha = len(data) / (len(stats.keys()) + 1.0)
        [mu, sigma, alpha], cov = opt.curve_fit(gauss, stats.keys(), stats.values(), p0=[guessMu, guessSigma, guessAlpha])
        plt.plot(
            [x for x in range(int(mu - sigmaWidth * sigma), int(mu + sigmaWidth * sigma))],
            [gauss(x, mu, sigma, alpha) for x in
                range(int(mu - sigmaWidth * sigma), int(mu + sigmaWidth * sigma))],
            color=colorArray[classID]
        )
        plt.hist(data, len(stats), color=colorArray[classID])
        classID += 1



dataToPlot = np.transpose(np.vstack((data[:, 1], data[:, 2])))
dataWOutNans = dataToPlot[~np.isnan(dataToPlot[:, 1])]

dataLying = dataWOutNans[dataWOutNans[:, 0] == 1][:, 1]
dataStanding = dataWOutNans[dataWOutNans[:, 0] == 3][:, 1]
dataRunning = dataWOutNans[dataWOutNans[:, 0] == 5][:, 1]

plotDataClassOverview([dataLying, dataStanding, dataRunning])

plt.show()