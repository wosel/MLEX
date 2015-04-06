import getopt
import pandas as pd
import numpy as np
import sys
import math
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

from sklearn.tree import DecisionTreeClassifier

from sklearn.cross_validation import train_test_split


class dataSet:
    def __init__(self, trainData, trainClasses, testData, testClasses):
        self.trainData = trainData
        self.trainClasses = trainClasses
        self.testData = testData
        self.testClasses = testClasses
    def getTest(self):
        return self.testData, self.testClasses
    def getTrain(self):
        return self.trainData, self.trainClasses
    def getTrain(self, count):
        trainDataPart = self.trainData[:count, :]
        trainClassesPart = self.trainClasses[:count]
        return trainDataPart, trainClassesPart
    def getTrainSize(self):
        return len(self.trainClasses)

class dataLoader:
    def __init__(self):
        self.dataset = self.loadData()

class creditData(dataLoader):

    def loadData(self):

        train = np.loadtxt('credit.train.txt', delimiter=',')
        trainData = train[:, :-1]
        trainClasses = train[:, -1]

        test = np.loadtxt('credit.test.txt', delimiter=',')
        testData = test[:, :-1]
        testClasses = test[:, -1]
        return dataSet(trainData, trainClasses, testData, testClasses)

class shapeData(dataLoader):
    def loadData(self):
        trainDF = pd.read_csv('clouds1k_train.csv');
        trainMat = trainDF.values
        trainData = trainMat[:, 2:-1].astype(np.float64)
        trainClasses = trainMat[:, -1].astype(np.int)

        testDF = pd.read_csv('clouds1k_test.csv');
        testMat = testDF.values
        testData = testMat[:, 2:-1].astype(np.float64)
        testClasses = testMat[:, -1].astype(np.int)
        return dataSet(trainData, trainClasses, testData, testClasses)

class AESOPData(dataLoader):
    def loadData(self):

        fullDF = pd.read_csv('AESOP.csv', index_col=False)
        fullDF.replace(to_replace='-1', value='0', inplace=True)
        categoricalCols = [
            'region',
            'student_until',
            'school_type_0', 'school_region_0',
            'school_type_1', 'school_region_1',
            'school_type_2', 'school_region_2'
        ]

        categoricalDF = fullDF.loc[:, categoricalCols]
        nonNumericalCols = categoricalCols[:]
        nonNumericalCols.append('student')
        numericalDF = fullDF.drop(nonNumericalCols,  1)

        classDF = fullDF.loc[:, 'student']

        dataDF = numericalDF
        for col in categoricalCols:
            colDF = pd.get_dummies(categoricalDF.loc[:, col])
            tmpDF = dataDF.join(colDF, rsuffix='_'+col)
            dataDF = tmpDF


        dataMat = dataDF.values
        classMat = classDF.values
        trainData, testData, trainClasses, testClasses = train_test_split(dataMat, classMat, test_size=.4)
        return dataSet(trainData, trainClasses, testData, testClasses)

class incomeData(dataLoader):
    def loadData(self):
        labels = [
            'age',
            'workclass',
            'fnlwgt',
            'education',
            'education-num',
            'marital-status',
            'occupation',
            'relationship',
            'race',
            'sex',
            'capital-gain',
            'capital-loss',
            'hours-per-week',
            'native-country',
            'loan'
        ]
        numericalCols = [
            'age',
            'fnlwgt',
            'education-num',
            'capital-gain',
            'capital-loss',
            'hours-per-week'
        ]
        categoricalCols = [
            'workclass',
            'education',
            'marital-status',
            'occupation',
            'relationship',
            'race',
            'sex',
            'native-country',
        ]
        trainDF = pd.read_csv('adult.data', header=None, names=labels)
        testDF = pd.read_csv('adult.test', header=None, names=labels)

        fullDF = pd.concat([trainDF, testDF])
        fullDF = fullDF.reset_index(drop=True)
        categoricalDF = fullDF.loc[:, categoricalCols]
        numericalDF = fullDF.loc[:, numericalCols]
        classDF = fullDF.loc[:, 'loan']

        dataDF = numericalDF
        for col in categoricalCols:
            colDF = pd.get_dummies(categoricalDF.loc[:, col])
            tmpDF = dataDF.join(colDF, rsuffix='_'+col)
            dataDF = tmpDF

        dataMat = dataDF.values
        classMat = classDF.values
        trainData, testData, trainClasses, testClasses = train_test_split(dataMat, classMat, test_size=.4)
        return dataSet(trainData, trainClasses, testData, testClasses)



dataLoaders = [
    creditData(),
    shapeData(),
    AESOPData(),
    incomeData()
]

dataSetNames = [
    "Credit ",
    "Generated pointclouds",
    "AESOP",
    "Adult income"
]

def runClassifier(clf, trainData, trainClasses, testData, testClasses):
    clf.fit(trainData, trainClasses)
    trainScore = clf.score(trainData, trainClasses)
    testScore = clf.score(testData, testClasses)
    return trainScore, testScore

def getPlotDimensions(plotCount, screenW, screenH):
    plotH = math.sqrt(screenH*plotCount/screenW)
    plotW = (screenW/screenH) * plotH

    floorH = int(math.floor(plotH))
    floorW = int(math.floor(plotW))

    if ((floorH+1) * floorW >= plotCount):
        return floorW, floorH+1
    elif (floorH * (floorW+1) >= plotCount):
        return floorW+1, floorH
    else:
        return floorW+1, floorH+1


def main():

    screenWidth = 16.
    screenHeight = 9.
    numSteps = 50


    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hn:w:g:', ['help', 'num-steps', 'screen-width=', 'screen-height='])
    except getopt.GetoptError:
        print 'diagnostics.py [-n <numSteps>] [-w <screenWidth>] [-h <screenHeight>]'
        return 1
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'diagnostics.py [-n <numSteps>] [-w <screenWidth>] [-h <screenHeight>]'
            break
        elif opt in('-n', '--num-steps'):
            numSteps = int(arg)
        elif opt in('-w', '--screen-width'):
            screenWidth = float(arg)
        elif opt in('-g', '--screen-height'):
            screenHeight = float(arg)


    # prepare the plot dimensions (when not given, assumes screen ration 16:9, will work reasonably well elsewhere)
    plotH, plotW = getPlotDimensions(len(dataLoaders), screenW=screenWidth, screenH=screenHeight)

    # lower bound on training set size - some algorithms need >1 data point. 10 is safe
    lowerBound = 10


    dataID = 0
    for dataL in dataLoaders:

        dataset = dataL.dataset
        stepSize = (dataset.getTrainSize()-lowerBound) / numSteps

        # prepare the subplot
        plt.subplot(plotH, plotW, dataID+1)
        plt.axis([0,numSteps,0,1])
        plt.ion()
        plt.title(dataSetNames[dataID])
        redLine = mlines.Line2D([], [], color='red', label='Training acc.')
        blueLine = mlines.Line2D([], [], color='blue', label='Testing acc.')
        plt.legend(handles=[blueLine, redLine], loc=4, prop={'size': 12})
        plt.show()

        # load test data, prepare scoring tables
        testData, testClasses = dataset.getTest()
        trainScoreTable = []
        testScoreTable = []

        # we have chosen the Decision Tree Classifier. You may substitute any classifier of choice
        clf = DecisionTreeClassifier(max_depth=5)


        for i in range(lowerBound, dataset.getTrainSize(), stepSize):
            # get the training data of the given size
            trainData, trainClasses = dataset.getTrain(i)

            # run the classifier, obtain score on training and testing data
            trainScore, testScore = runClassifier(clf, trainData, trainClasses, testData, testClasses)


            # append to result tables
            trainScoreTable.append(trainScore)
            testScoreTable.append(testScore)

            # plot results so far
            plt.plot(trainScoreTable, 'r-', label='Training acc.')
            plt.plot(testScoreTable, 'b-', label='Testing acc.')
            plt.draw()
            plt.pause(0.001)

        dataID += 1

    # Wait for user to close pyplot figure beofre exiting
    plt.show(block=True)



if __name__ == "__main__":
    sys.exit(main())
