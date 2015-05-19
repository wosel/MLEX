import copy
import numpy as np
import random
import sys


class classicalKMeans:
    def __init__(self, k):
        self.k = k;


    def fit(self, X):


        self.cluster_centers_ = np.empty((self.k, X.shape[1]))
        for center in range(self.k):
            self.cluster_centers_[center] = X[random.randrange(X.shape[0]),:]

        assignments = np.zeros(X.shape[0])
        newAssignments = np.zeros(X.shape[0])
        assigmentsChanged = True
        while (assigmentsChanged):
            new_cluster_centers = np.zeros((self.k, X.shape[1]))
            new_cc_counts = np.zeros(self.k)
            for sampleIdx in range(X.shape[0]):
                x = X[sampleIdx, :]
                label = self.assign(x)
                new_cluster_centers[label, :] += x
                new_cc_counts[label] += 1
                newAssignments[sampleIdx] = label
            assigmentsChanged = False
            for sampleIdx in range(X.shape[0]):
                if (assignments[sampleIdx] != newAssignments[sampleIdx]):
                    assigmentsChanged = True
            assignments = copy.deepcopy(newAssignments)
            for ccIdx in range(self.k):
                if (new_cc_counts[ccIdx] == 0):
                    new_cluster_centers[ccIdx, :] = X[random.randrange(X.shape[0]),:]
                else:
                    new_cluster_centers[ccIdx, :]  /= new_cc_counts[ccIdx]
            self.cluster_centers_ = new_cluster_centers



    def predict(self, X):
        self.labels_ = np.empty((X.shape[0]), dtype=int)
        for sampleIdx in range(X.shape[0]):
            x = X[sampleIdx, :]
            self.labels_[sampleIdx] = self.assign(x)
        return self.labels_

    def assign(self, x):
        minCC = -1
        ccIdx = 0
        minCCIdx = -1
        minDist = sys.float_info.max
        for cCenter in self.cluster_centers_:
            dist = np.linalg.norm(x - cCenter)
            if (dist < minDist):
                minDist = dist
                minCC = cCenter
                minCCIdx = ccIdx;

            ccIdx += 1

        return minCCIdx


    def fit_predict(self, X):
        self.fit(X)
        return self.predict(X)