import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.lda import LDA

import sys


names = ["Nearest Neighbors",
         "RBF SVM",
         "Decision Tree",
         "Random Forest",
         "AdaBoost",
         ]
classifiers = [
    KNeighborsClassifier(3),
    SVC(gamma=2, C=1),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    AdaBoostClassifier(),

    ]
def creditData():

    train = np.loadtxt('credit.train.txt', delimiter=',')
    trainData = train[:, :-1]
    trainClasses = train[:, -1]

    test = np.loadtxt('credit.test.txt', delimiter=',')
    testData = test[:, :-1]
    testClasses = test[:, -1]

    for name, clf in zip(names, classifiers):
        clf.fit(trainData, trainClasses)
        score = clf.score(testData, testClasses)
        print name, score

def shapeData():

    trainDF = pd.read_csv('clouds1k_train.csv');
    trainMat = trainDF.values
    trainData = trainMat[:, 2:-1].astype(np.float64)
    trainClasses = trainMat[:, -1].astype(np.int)

    testDF = pd.read_csv('clouds1k_test.csv');
    testMat = testDF.values
    testData = testMat[:, 2:-1].astype(np.float64)
    testClasses = testMat[:, -1].astype(np.int)
    for name, clf in zip(names, classifiers):
        clf.fit(trainData, trainClasses)
        score = clf.score(testData, testClasses)
        print name, score



def AESOPData():

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
    for name, clf in zip(names, classifiers):
        clf.fit(trainData, trainClasses)
        score = clf.score(testData, testClasses)
        print name, score


def incomeData():
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

    for name, clf in zip(names, classifiers):
        clf.fit(trainData, trainClasses)
        score = clf.score(testData, testClasses)
        print name, score

def main():
    print "Credit data results:"
    creditData()
    print "\nShape data results:"
    shapeData()
    print "\nAESOP data results:"
    AESOPData()
    print "\nIncome data results:"
    incomeData()

if __name__ == "__main__":
    sys.exit(main())

