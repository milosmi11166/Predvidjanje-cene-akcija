import csv
import random
import math
import operator

import pandas_datareader.data as web
import datetime
import pandas as pd

import matplotlib.pyplot as plt   # Import matplotlib
import json



def loadDataset(filename, split, trainingSet=[], testSet=[], content_header=[]):
    with open(filename, 'rb') as csvfile:
     
        lines = csv.reader(csvfile)
		
        dataset = list(lines)
        for x in range(len(dataset) - 1):
		
            for y in range(1, len(content_header) - 1):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])



def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(1, length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


# get k nearest neighbors 
# trainingSet
def getNeighbors(trainingSet, testInstance, k):
    distance = []

    length = len(testInstance) - 1

    for x in range((len(trainingSet))):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distance.append((trainingSet[x], dist))
    distance.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distance[x][0])
    return neighbors


def main():
    split = 0.67
    # set data
    startdate = datetime.datetime(2002,1,1)
    enddate = datetime.date.today()

    predictFor(5, 'amtd.csv', 'AMTD', startdate, enddate, 0, split)
    
main()
