import numpy as np
import pandas as pd
from sklearn.svm import SVC
import time
from sklearn.preprocessing import StandardScaler
from sklearn import grid_search
import sys
import matplotlib.pyplot as plt
import getopt


def runGridSearch(params, trainData, trainClasses, numJobs, verboseLevel, crossValFolds):
    maxIters = 10000

    estimator = SVC(max_iter=maxIters)
    clf = grid_search.GridSearchCV(estimator, params, n_jobs=numJobs, pre_dispatch='n_jobs', verbose=verboseLevel, cv=crossValFolds)
    clf.fit(trainData, trainClasses)
    return clf

def preparePlotBase(paramsRBF, scores):

    cValHash = {}
    i = 0
    for cVal in paramsRBF['C']:
        cValHash[cVal] = i
        i += 1

    gammaValHash = {}
    i = 0
    for gammaVal in paramsRBF['gamma']:
        gammaValHash[gammaVal] = i
        i += 1

    plotBase = np.zeros([len(cValHash), len(gammaValHash)])
    for p in scores:
        params = p[0]
        mean = p[1]
        cIdx = cValHash[params['C']]
        gammaIdx = gammaValHash[params['gamma']]
        plotBase[cIdx, gammaIdx] = mean

    return plotBase



def main():

    filename = ''
    processCount = 2
    classCol = -1
    crossValFolds = 3
    verboseLevel = 1
    separator=' '
    header = False

    run10fold = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hdf:s:l:p:c:v:r', ['help', 'header' 'filename=', 'separator=', 'classCol=', 'processCount=', 'crossValFolds=', 'verboseLevel=', 'run10fold'])
    except getopt.GetoptError:
        print "getopt error"
        print 'kernels.py -f <filename>  -s <separator> -d <header> -l <classCol> -p <processCount> -c <crossValFolds> -v <verboseLevel>'
        return 1
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'kernels.py -f <filename> -s <separator> -d <header> -l <classCol> -p <processCount> -c <crossValFolds> -v <verboseLevel>'
            break
        elif opt in('-f', '--filename'):
            filename = arg
        elif opt in('-s', '--separator'):
            separator = arg
        elif opt in('-p', '--processCount'):
            processCount = int(arg)
        elif opt in ('-l', '--classCol'):
            classCol = int(arg)
        elif opt in ('-c', '--crossValFolds'):
            crossValFolds = int(arg)
        elif opt in('-v', '--verboseLevel'):
            verboseLevel = int(arg)
        elif opt in ('-d', '--header'):
            header = True
        elif opt in ('-r', '--run10fold'):
            run10fold = True


    if (filename == '' or classCol == -1):
        print "missing filename or classCol"
        print 'kernels.py -f <fileName> -s <separator> -d <header> -l <classCol> -p <processCount> -c <crossValFolds> -v <verboseLevel>'
        return 1
    fullDF = pd.DataFrame
    if (header):
        fullDF = pd.read_csv(filename, sep=separator)
    else:
        fullDF = pd.read_csv(filename, sep=separator, header=None)
    fullDF = fullDF.dropna()
    allData = fullDF.as_matrix()
    allClasses = allData[:, classCol]
    allFeatures = np.delete(arr=allData, obj=classCol, axis=1)
    scaler = StandardScaler()
    allFeatures = scaler.fit_transform(allFeatures)




### PART ONE: linear vs. polynomial vs. RBF
    paramsKernels = dict(
        kernel=('linear', 'poly', 'rbf'),
    )
    clf = runGridSearch(paramsKernels, allFeatures, allClasses, numJobs=processCount, verboseLevel=verboseLevel, crossValFolds=crossValFolds)
    print "Best kernel was {0} with a score of {1}".format(clf.best_params_['kernel'], clf.best_score_)


### PART TWO & THREE: plotting a heatmap and choosing the best RBF parameters
    paramsRBF = dict(
        kernel=['rbf'],
        C=(0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000),
        gamma=(0.0001, 0.001, 0.01, 0.1, 1, 10, 100)
    )
    clf = runGridSearch(paramsRBF, allFeatures, allClasses, numJobs=processCount, verboseLevel=verboseLevel, crossValFolds=crossValFolds)
    plotBase = preparePlotBase(paramsRBF, clf.grid_scores_)
    plt.pcolor(plotBase, cmap=plt.cm.Reds)
    plt.xticks(np.arange(0,len(paramsRBF['gamma']))+0.5,paramsRBF['gamma'])
    plt.yticks(np.arange(0,len(paramsRBF['C']))+0.5,paramsRBF['C'])
    plt.ylabel('C', fontsize=20)
    plt.xlabel('gamma', fontsize=20)
    plt.show()

    print "Best rbf kernel had C = {0} and gamma = {1}, and achieved a score of {2}".format(clf.best_params_['C'], clf.best_params_['gamma'], clf.best_score_)

### OPTIONAL PART FOUR: run the same with n-fold cross-validation
### just the same as part two, but with more cross validation folds (10) and more numbers
    if (run10fold):
        paramsRBF = dict(
            kernel=['rbf'],
            C=(0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000),
            gamma=(0.0001, 0.001, 0.01, 0.1, 1, 10, 100)
        )
        clf = runGridSearch(paramsRBF, allFeatures, allClasses, numJobs=processCount, verboseLevel=verboseLevel, crossValFolds=10)
        for p in clf.grid_scores_:
            print "RBF kernel with C {0} and gamma {1} had mean {2} and stdev {3}".format(p[0]['C'], p[0]['gamma'], p[1], np.std(p[2]))
        plotBase = preparePlotBase(paramsRBF, clf.grid_scores_)

        plt.pcolor(plotBase, cmap=plt.cm.Blues)
        plt.xticks(np.arange(0,len(paramsRBF['gamma']))+0.5,paramsRBF['gamma'])
        plt.yticks(np.arange(0,len(paramsRBF['C']))+0.5,paramsRBF['C'])
        plt.ylabel('C', fontsize=20)
        plt.xlabel('gamma', fontsize=20)
        plt.show()




if __name__ == "__main__":
    sys.exit(main())
