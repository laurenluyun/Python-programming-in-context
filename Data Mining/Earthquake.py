# -*- coding = utf-8 -*-
# @Time : 5/17/2023 1:51 PM
# @Author : Lauren
# @File : Earthquake.py
# @Software : PyCharm

import csv
import turtle
from KMeansAlgo import createCentroids, createClusters

def readPrint():
    with open("earthquakes.csv", "r") as dataFile:
        csvReader = csv.reader(dataFile) # get the iterator
        titles = next(csvReader) # read titles line
        print("titles: ", titles) # output titles

        # read the first earthquake line in list
        earthquakeLine = next(csvReader)
        # output all data in list
        print("earthquake:", earthquakeLine)
        # output the latitude
        print("latitude: ", earthquakeLine[1])
        # output the longitude
        print("longitude: ", earthquakeLine[2])

def readEarthquakeFile(filename):
    '''
    this function is to read the filename and return lat and long in a
    dictionary
    :param filename:
    :return: dictionary
    '''
    with open(filename, "r") as dataFile:
        csvReader = csv.reader(dataFile)
        titles = next(csvReader) # read and skip titles
        dataDict = {}
        key = 0

        for aLine in csvReader:
            key += 1 # key is the line number
            lat = float(aLine[1]) # extract the first element of each line
            # as the lat
            long = float(aLine[2])
            dataDict[key] = [long, lat]
    return dataDict

'''
The next step is to leverage the cluster analysis in KMeansAlgo.py
then visualize each cluster with different colors in a map in turtle
'''

def visualizeQuakes(dataFile):
    dataDict = readEarthquakeFile(dataFile)
    quakeCentroids = createCentroids(6, dataDict)
    # create 6 clusters for the data under 7 repetition
    clusters = createClusters(6, quakeCentroids, dataDict, 7)

    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic("worldmap.gif")
    quakeWin.screensize(448, 252)

    # the lower-left corner of the map should be location (-180, -90)
    # and the upper-right corner should be (180, 90)
    wFactor = (quakeWin.screensize()[0] / 2 ) / 180
    hFactor = (quakeWin.screensize()[1] / 2) / 90

    quakeT.hideturtle()
    quakeT.up()

    colorList = ["red", "lawngreen", "blue", "orange", "cyan", "yellow"]

    for clusterIndex in range(6):
        quakeT.color(colorList[clusterIndex]) # choose cluster color
        for aKey in clusters[clusterIndex]:
            lon = dataDict[aKey][0]
            lat = dataDict[aKey][1]
            quakeT.goto(lon * wFactor, lat * hFactor)
            # draw the dot
            quakeT.dot()

    quakeWin.exitonclick()

def main():
    visualizeQuakes("earthquakes.csv")

if __name__ == "__main__":
    main()