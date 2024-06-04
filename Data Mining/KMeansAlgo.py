# -*- coding = utf-8 -*-
# @Time : 5/16/2023 8:13 PM
# @Author : Lauren
# @File : KMeansAlgo.py
# @Software : PyCharm
import math
import random

def euclidD(point1, point2):
    # helper function to compute the distance between two points
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total += diff
    euclidDistance = math.sqrt(total)

    return euclidDistance


def readFile(filename):
    # helper function to read the file and return non-empty line in
    # dictionary with the order as key
    with open(filename, "r") as dataFile:
        dataDict = {}
        key = 0
        # use .readline method to get the next line of the file
        aline = dataFile.readline()
        while aline != "":
            key += 1
            dataDict[key] = [int(aline)]
            aline = dataFile.readline()
    return dataDict

def createCentroids(k, dataDict):
    '''
    The helper function implements the centroid selection process
    which is to fill the list with k randomly selected data points
    from the dataDict
    return: a list of k random centroids
    '''
    centroids = []
    centroidCount = 0
    centroidKeys = []
    while centroidCount < k:
        rKey = random.randint(1, len(dataDict))
        if rKey not in centroidKeys:
            centroids.append(dataDict[rKey])
            centroidKeys.append(rKey)
            centroidCount += 1
    return centroids

def createClusters(k, centroids, dataDict, repeats):
    '''
    This is function is to create the clusters.
    parameters:
        k: the number of clusters
        centroids: the previously created list of k centroids
        dataDic
        repeats: the number of repetitions
    returns:
        a list of the clusters
    '''
    # for loop to implement the process for repeats number
    # of times
    for aPass in range(repeats):
        # denotes the current iteration
        print("****PASS", aPass + 1, "****")

        # ini a nested list of k clusters
        clusters = []
        # create a list of k empty clusters which are also lists
        for i in range(k):
            clusters.append([])

        # for loop - for every point in the dataDict, calculate the distance
        # to every centroid=> restore in the distances list for every point
        # => find the minium distance and the respective index => the index
        # denotes the index of the respective cluster for this point to be
        # clustered in (find the cluster for this point) => assign each
        # point to the cluster with the closest centroid
        for aKey in dataDict:
            distances = []
            for clusterIndex in range(k):
                # compute the distance between the current point and the
                # current centroid (for each cluster there are k centroids)
                # dToc = euclidD(dataDict[aKey], centroids[clusterIndex])
                # the dist method accepts its parameters as equal-length
                # tuples
                dtoC = math.dist(tuple(dataDict[aKey]), tuple(centroids[
                                                                  clusterIndex]))
                distances.append(dtoC)

            minDist = min(distances) # find the minium distance
            # and the respective index of the minimum distance, which tells
            # the cluster to which the data point should belong
            index = distances.index(minDist)

            # we can access the list of clusters and append the key to the
            # proper cluster
            clusters[index].append(aKey)

        # final step is to recompute the centroids for each cluster
        # since the centroid of a cluster is simply the average of all data
        # points in the cluster, we can iterate through the points, create
        # a running sum, and then divide by the number of points.
        dimensions = len(dataDict[1]) # the datapoint can be
        # multidimensional, dimensions is the number of dimensions within
        # the data point, in this case, the dimension is 1

        # for loop to traverse through every cluster, for each cluster,
        # get the sum of each dimension of each data point (here is only 1
        # dimension) [note: dataPoints itself is a list]
        for clusterIndex in range(k):
            # ini sum - a list of dimensions number of elements with value 0
            # dimension - x, y, z... in coordinates
            sums = [0] * dimensions
            # for loop to traverse through every point in the current cluster
            # and get the sum of the value of each dimension (here is only 1)
            for aKey in clusters[clusterIndex]:
                # get the value of the current point
                dataPoints = dataDict[aKey]
                # get the sum of the each dimension of the current data point
                for ind in range(len(dataPoints)):
                    sums[ind] += dataPoints[ind]

            # calculate the average of each dimension for each cluster
            for ind in range(len(sums)):
                # get the number of data points in each cluster
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    # replace the sum of dimension with its average through
                    # the current cluster
                    sums[ind] = sums[ind] / clusterLen

            # assign the average to the proper position in the centroids list
            centroids[clusterIndex] = sums

        # print each cluster with the value of its data points in each pass
        for each in clusters:
            print("CLUSTER")
            for key in each:
                print(dataDict[key], end = " ")
            print()

    return clusters

def clusterAnalysis(dataFile):
    examDict = readFile(dataFile)
    examCentroids = createCentroids(5, examDict) # 5 clusters and 5 centroids
    examClusters = createClusters(5, examCentroids, examDict, 3) # repeat 3
    # times

def main():
    clusterAnalysis("cs150exams.txt")

if __name__ == "__main__":
    main()