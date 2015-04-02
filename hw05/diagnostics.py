import pandas as pd
import numpy as np
import sys

import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

from sklearn.cross_validation import train_test_split


names = ["Nearest Neighbors",
#         "RBF SVM",
#         "Decision Tree",
#         "Random Forest",
#         "AdaBoost",
         ]
classifiers = [
    KNeighborsClassifier(3),
#    SVC(gamma=2, C=1),
#    DecisionTreeClassifier(max_depth=5),
#    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
#    AdaBoostClassifier(),
]

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
        pass

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
#    shapeData(),
#    AESOPData(),
#    incomeData()
]


def runClassifier(clf, trainData, trainClasses, testData, testClasses):
    clf.fit(trainData, trainClasses)
    trainScore = clf.score(trainData, trainClasses)
    testScore = clf.score(testData, testClasses)
    return trainScore, testScore


def main():

    for dataL in dataLoaders:
        print dataL

        dataset = dataL.loadData()

        stepSize = dataset.getTrainSize() / 100
        plt.axis([0,100,0,1])

        plt.ion()
        plt.show()
        testData, testClasses = dataset.getTest()
        for (name, clf) in zip(names, classifiers):
            print name
            trainScoreTable = []
            testScoreTable = []
            for i in range(10, dataset.getTrainSize(), stepSize):
                trainData, trainClasses = dataset.getTrain(i)
                trainScore, testScore = runClassifier(clf, trainData, trainClasses, testData, testClasses)
                trainScoreTable.append(trainScore)
                testScoreTable.append(testScore)
                plt.plot(trainScoreTable, 'r-', testScoreTable, 'b-')
                plt.draw()




if __name__ == "__main__":
    sys.exit(main())
