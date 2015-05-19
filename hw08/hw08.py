import sys

import time

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import kMeans

import pandas as pd

from sklearn import cluster, datasets, metrics
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler

#############  Following code taken from example @ scikit-learn.org ############
def bench_k_means(estimator, name, labels):

    scores = {
        "homogeneity": metrics.homogeneity_score(labels, estimator.labels_),
        "completeness": metrics.completeness_score(labels, estimator.labels_),
        "v_measure": metrics.v_measure_score(labels, estimator.labels_),
        "ARI": metrics.adjusted_rand_score(labels, estimator.labels_),
        "AMI": metrics.adjusted_mutual_info_score(labels,  estimator.labels_)



    }
    return scores

#############  End of code taken from example @ scikit-learn.org ###############

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

class pamapData:
    def __init__(self):
        self.dataset = self.loadData();
    def loadData(self):
        trainDF = pd.read_csv('pamap_easy.train.txt', delimiter='\t', header=None)
        trainMat = trainDF.values
        trainData = trainMat[:, 0:2]
        trainClasses = trainMat[:, 2]

        testDF = pd.read_csv('pamap_easy.test.txt', delimiter='\t', header=None)
        testMat = testDF.values
        testData = testMat[:, 0:2]
        testClasses = testMat[:, 2]
        return dataSet(trainData, trainClasses, testData, testClasses)

class origData:
    def __init__(self, data, labels):
        self.data_ = data
        self.labels_ = labels
    def fit(self, X):
        pass
    def predict(self, X):
        return self.labels_

    def fit_predict(self, X):
        self.fit(X)
        return self.predict(X)

def runComparisonOnDataset(dataLoader):


    pamapDataSet = dataLoader.dataset

    X, y = pamapDataSet.getTrain(3900)
    #X = pamapDataSet.trainData
    #y = pamapDataSet.trainClasses


    numTrueClusters = len(set(y))
    myKMeans = kMeans.classicalKMeans(numTrueClusters);

#############  Following code taken from example @ scikit-learn.org ############


    # normalize dataset for easier parameter selection
    X = StandardScaler().fit_transform(X)



    orig = origData(X, y)

    # estimate bandwidth for mean shift
    bandwidth = cluster.estimate_bandwidth(X, quantile=0.3)

    # connectivity matrix for structured Ward
    connectivity = kneighbors_graph(X, n_neighbors=10)
    # make connectivity symmetric
    connectivity = 0.5 * (connectivity + connectivity.T)

    # create clustering estimators
    ms = cluster.MeanShift(bandwidth=bandwidth, bin_seeding=True)
    two_means = cluster.MiniBatchKMeans(n_clusters=numTrueClusters)
    ward = cluster.AgglomerativeClustering(n_clusters=numTrueClusters, linkage='ward',
                                           connectivity=connectivity)
    spectral = cluster.SpectralClustering(n_clusters=numTrueClusters,
                                          eigen_solver='arpack',
                                          affinity="nearest_neighbors")
    dbscan = cluster.DBSCAN(eps=.2)
    affinity_propagation = cluster.AffinityPropagation(damping=.9,
                                                       preference=-200)

    average_linkage = cluster.AgglomerativeClustering(
        linkage="average", affinity="cityblock", n_clusters=numTrueClusters,
        connectivity=connectivity)

    clustering_names = [
        'Original', 'MiniBatchKMeans', 'MY_K_MEANS', 'MeanShift',
        'SpectralClustering', 'Ward', 'AgglomerativeClustering',
        'DBSCAN']

    clustering_algorithms = [
        orig, two_means, myKMeans,  ms, spectral, ward, average_linkage,
        dbscan]


    # plot setup
    plt.figure(figsize=(len(clustering_names) * 2 + 3, 9.5))
    plt.subplots_adjust(left=.02, right=.98, bottom=.001, top=.96, wspace=.05,
                        hspace=.01)
    plot_num = 1
    colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
    colors = np.hstack([colors] * 20)

    scores = dict()
    for name, algorithm in zip(clustering_names, clustering_algorithms):
        # predict cluster memberships
        t0 = time.time()
        algorithm.fit(X)
        t1 = time.time()
        if hasattr(algorithm, 'labels_'):
            y_pred = algorithm.labels_.astype(np.int)
        else:
            y_pred = algorithm.predict(X)

        if hasattr(algorithm, 'labels_'):
            scores[name] = bench_k_means(algorithm, name, y)

        # plot
        plt.subplot(4, len(clustering_algorithms), plot_num)

        plt.title(name, size=18)
        plt.scatter(X[:, 0], X[:, 1], color=colors[y_pred].tolist(), s=10)

        if hasattr(algorithm, 'cluster_centers_'):
            centers = algorithm.cluster_centers_
            center_colors = colors[:len(centers)]
            plt.scatter(centers[:, 0], centers[:, 1], s=100, c=center_colors)
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        plt.xticks(())
        plt.yticks(())
        plt.text(.99, .01, ('%.2fs' % (t1 - t0)).lstrip('0'),
                 transform=plt.gca().transAxes, size=15,
                 horizontalalignment='right')
        plot_num += 1


    scoredf = pd.DataFrame(scores)
    print scoredf.transpose()
    plt.show()

#############  End of code taken from example @ scikit-learn.org ###############


def main():
    pamapLoader = pamapData()

    runComparisonOnDataset(dataLoader=pamapLoader)

if __name__ == "__main__":
    sys.exit(main())

