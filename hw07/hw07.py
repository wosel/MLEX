import getopt
import pandas as pd
import numpy as np
import sys
import math
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

from sklearn.feature_extraction import DictVectorizer


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


class artificialData(dataLoader):
    def loadData(self):
        trainDF = pd.read_csv('artificial_2x_train.tsv', delimiter = '\t', header=None)
        train = trainDF.values
        trainFeatures = train[:, :-1]
        trainValues = train[:, -1]

        testDF = pd.read_csv('artificial_2x_test.tsv', delimiter = '\t', header=None)
        test = testDF.values
        testFeatures = test[:, :-1]
        testValues = test[:, -1]


        return dataSet(trainFeatures, trainValues, testFeatures, testValues)

def normalizeColumns(inputMatrix):
    outputMatrix = np.empty(shape=inputMatrix.shape)
    maxVal = np.ones([1, inputMatrix.shape[1]])[0, :] * sys.float_info.min
    minVal = np.ones([1, inputMatrix.shape[1]])[0, :] * sys.float_info.max
    sum = np.zeros([1, inputMatrix.shape[1]])[0, :]
    for i in range(inputMatrix.shape[0]):
        dataSample = inputMatrix[i, :]
        for j in range(len(dataSample)):
            if (inputMatrix[i, j] > maxVal[j]): maxVal[j] = inputMatrix[i, j]
            if (inputMatrix[i, j] < maxVal[j]): minVal[j] = inputMatrix[i, j]
            sum[j] += inputMatrix[i, j]
    avg = sum / inputMatrix.shape[0]
    for i in range(inputMatrix.shape[0]):
        dataSample = inputMatrix[i, :]
        for j in range(len(dataSample)):
            outputMatrix[i, j] = (inputMatrix[i, j] - avg[j]) / (maxVal[j] - minVal[j])
    return outputMatrix



class realEstateData(dataLoader):
    def loadData(self):
        trainDF = pd.read_csv('pragueestateprices_train.tsv', delimiter = r"\s+", header=None, names=['size', 'building', 'owner', 'state', 'floor', 'furnished', 'basement', 'balcony', 'price'])
        trainDFValues = trainDF.loc[:, 'price']
        trainDF.drop('price', 1, inplace=True)
        trainDict = trainDF.T.to_dict().values()

        testDF = pd.read_csv('pragueestateprices_test.tsv', delimiter = r"\s+", header=None, names=['size', 'building', 'owner', 'state', 'floor', 'furnished', 'basement', 'balcony', 'price'])
        testDFValues = testDF.loc[:, 'price']
        testDF.drop('price', 1, inplace=True)
        testDict = testDF.T.to_dict().values()

        dv = DictVectorizer(sparse=False)

        fullDF = pd.concat([trainDF, testDF])
        fullDict = fullDF.T.to_dict().values()
        fittedDV = dv.fit(fullDict)


        train = fittedDV.transform(trainDict)
        test = fittedDV.transform(testDict)

        trainNorm = normalizeColumns(train)
        testNorm = normalizeColumns(test)

        return dataSet(trainNorm, trainDFValues.values / 10**6,  testNorm, testDFValues.values / 10**6)



class SGDRegression():
    def __init__(self, learnRate, gradientLimit):
        self.learnRate = learnRate
        self.gradientLimit = gradientLimit
    def fit(self, features, values):
        paramCount = features.shape[1] + 1
        self.theta = np.zeros([1, paramCount])[0, :]
        gradient = np.ones([1, paramCount])[0, :]
        while (np.dot(gradient, gradient.transpose()) > self.gradientLimit):
            i = np.random.randint(features.shape[0])
            dataSample = np.concatenate(([1], features[i, :]), axis=0)
            gradient = (np.dot(self.theta, dataSample.transpose()) - values[i]) * dataSample

            thetaTmp = self.theta - self.learnRate * (1./features.shape[0]) * (np.dot(self.theta, dataSample.transpose()) - values[i]) * dataSample
            self.theta = thetaTmp

    def MSE(self, features, values):
        err = 0.
        for i in range(features.shape[0]):
            dataSample = np.concatenate(([1], features[i, :]), axis=0)
            err += (np.dot(self.theta, dataSample.transpose()) - values[i]) ** 2
        err /= features.shape[0]
        return err


testCases = [
    {'name': "Artificial data", 'dataLoader': artificialData(), 'learnRate': 0.01, 'gradientLimit': 0.000001 },
    {'name': "Real Estate data", 'dataLoader': realEstateData(), 'learnRate': 0.01, 'gradientLimit': 0.0001 }


]



def main():
    for case in testCases:
        dataset = case['dataLoader'].dataset
        sgd = SGDRegression(case['learnRate'], case['gradientLimit'])
        sgd.fit(dataset.trainData, dataset.trainClasses)
        print "Dataset: {0}".format(case['name'])

        print "Train MSE: {0}".format(sgd.MSE(dataset.trainData, dataset.trainClasses))
        print "Test MSE: {0}".format(sgd.MSE(dataset.testData, dataset.testClasses))
        print ""





if __name__ == "__main__":
    sys.exit(main())
