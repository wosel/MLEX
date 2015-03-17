import random
import numpy as np
import sys
import getopt

def loadTrainingSet(filename):
    """
    Loads the training set

    :param filename: the filename to load the training set from
    :return: the loaded dataset as an arrray of values, row ~ data example, column ~ feature incl. class
    """
    fTrain = open(filename)
    data = []
    for line in fTrain:
        featuresTmp = line.rstrip().split(',')
        features = [x.strip() for x in featuresTmp]
        data.append(features)
    fTrain.close()
    return data

def discreteMetric(arrayA, arrayB):
    """
    calculates the discrete metric between two arrays
    d(x, y) = 0 iff x==y, = 1 otherwise

    :param arrayA:
    :param arrayB:
    :return: the distance ~ the number of elements in the array which difffered
    """
    if len(arrayA) != len(arrayB):
        print arrayA
        print arrayB
        raise RuntimeError("cannot compare different lengths arrays")
    dist = 0
    for i in range(len(arrayA)):
        if arrayA[i] != arrayB[i]:
            dist += 1
    return dist

def getDistMaps(testSample, data, classCol):
    """

    :param testSample: the sample from which we calculate the distance
    :param data: the (training / model) data
    :param classCol: (which column of the dataset is the class)
    :return: the distMaps: distMaps[i] ~ list of datapoints with distance i from testSample
    """
    distMaps = [[] for _ in range(len(testSample))]
    for sample in data:
        sampleFeatures = sample[:classCol]+sample[classCol+1:]
        testSampleFeatures = testSample[:classCol]+testSample[classCol+1:]
        dist = discreteMetric(testSampleFeatures, sampleFeatures)
        distMaps[dist].append(sample)
    return distMaps


def getClassif(distMaps, classCol, k):
    """
    Predicts the class of a datapoint based on distMaps

    :param distMaps: the distMaps from a single testSample (see getDistMaps)
    :param classCol: what column of the data is the class in
    :param k: the 'k' in k-nearest neighbors
    :return: the predicted class
    """
    currentNeighbours = 0
    votes = {}
    for dist in range(len(distMaps)):
        distSize = len(distMaps[dist])
        if (currentNeighbours + distSize) <= k:
            #everybode gets to vote
            for trainSample in distMaps[dist]:
                if trainSample[classCol] in votes:
                    votes[trainSample[classCol]] += 1
                else:
                    votes[trainSample[classCol]] = 1
            currentNeighbours += distSize

        elif (currentNeighbours + distSize) > k:
            # only (k - currentNeighbours) get to vote
            # choose them randomly
            votingList = [distMaps[dist][i] for i in sorted(random.sample(xrange(distSize), k - currentNeighbours))]
            for trainSample in votingList:
                if trainSample[classCol] in votes:
                    votes[trainSample[classCol]] += 1
                else:
                    votes[trainSample[classCol]] = 1
                    #no need to carry on, found k neighbours
            break
    maxIdx = np.argmax(votes.values())
    classif = votes.keys()[maxIdx]
    return classif


def runOnTestData(trainedData, testFilename, classCol, k, verbose=False, reportInterval=100):
    """
    Runs the classification on a test dataset

    :param trainedData: the training / model data
    :param testFilename: the filename where the test data are
    :param classCol: w
    :param k: what column of the data is the class in
    :return: number of succesfully classified datapoints, and number of unsuccesfully classified datapoints
    """
    fTest = open(testFilename)
    succ = 0
    fail = 0
    counter = 0

    for line in fTest:
        if verbose and divmod(counter, reportInterval):
            print "Finished {0} datapoints with {1} succesfully classified".format(counter, succ)
        testSampleTmp = line.rstrip().split(',')
        testSample = [x.strip() for x in testSampleTmp]
        distMaps = getDistMaps(testSample, trainedData, classCol=classCol)
        classif = getClassif(distMaps, classCol, k=k)


        if classif == testSample[classCol]:
            succ += 1;
        else:
            if verbose:
                print "error: {0} classified as {1}".format(testSample, classif)
            fail += 1
        counter+=1
    return succ, fail



def main():
    trainFilename = ''
    testFilename = ''
    k = 1

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hr:s:k:c:', ['help', 'trainFile=' 'testFile=', 'k=', 'classCol='])
    except getopt.GetoptError:
        print 'knn.py -r <trainingFile> -s <testingFile> -k <k> -c <classCol>'
        return 1
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'knn.py -r <trainingFile> -s <testingFile> -k <k> -c <classCol>'
        elif opt in('-r', '--trainFile'):
            trainFilename = arg
        elif opt in('-s', '--testFile'):
            testFilename = arg
        elif opt in ('-k', '--k'):
            k = int(arg)
        elif opt in ('-c', '--classCol'):
            classCol = int(arg)
    if (trainFilename == '' or testFilename == ''):
        print 'knn.py -r <trainingFile> -s <testingFile> -k <k> -c <classCol>'
        return 1

    print ''

    print "training on " + trainFilename
    data = loadTrainingSet(trainFilename)
    print "trained (data loaded) from " + trainFilename

    print ''

    print "testing on " + testFilename + " with k set to " + str(k)
    successCt, failCt = runOnTestData(trainedData=data, testFilename=testFilename, classCol=classCol, k=k, verbose=True)

    print ''
    print "done: "
    print "succesful classifications: " + str(successCt)
    print "total cases: " + str(failCt+successCt)
    print "accuracy: " + str(float(successCt) / (failCt+successCt))


if __name__ == "__main__":
    sys.exit(main())
