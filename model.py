import math
import operator


from data_fetch import loadDataset, loadDatasetSeparate, getData
from plot import plotResults



def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(1, length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)



def getNeighborsWithWeights(trainingSet, testInstance, k):
    distance = []
    length = len(testInstance) - 1

    for x in range((len(trainingSet))):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distance.append((trainingSet[x], dist))

    distance.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distance[x])
    return neighbors



def mse(predicted, testSet):
    s = 0.0
    for i in range(len(predicted)):
	s += math.pow((predicted[i]-testSet[i][-1]), 2)
    return s / len(predicted)



def getRespWithWeights(neighbors):
    rec_dist_sq = 0.0
    for x in range(len(neighbors)):
	rec_dist_sq += (1/((neighbors[x][1])**2))

    response = 0.0
    for x in range(len(neighbors)):
	response += (((1/neighbors[x][1]**2)/rec_dist_sq)*neighbors[x][0][-1])
    return response



def predictFor(k, filename, stockname, startdate, enddate, writeAgain, split):
    iv = ["date", "open", "high", "low", "close adj", ""]
    trainingSet = []
    testSet = []

    if writeAgain:
        print("\nGetting data from yahoo finance..")
        getData(filename, stockname, startdate, enddate)

    loadDataset(filename, split, trainingSet, testSet, iv)

    print("\nPredicting for " + stockname)
    print("Train: " + repr(len(trainingSet)))
    print("Test: " + repr(len(testSet)))
    print("Total: " + repr(len(trainingSet) + len(testSet)))
    predictions = []
    for x in range(len(testSet)):
	print(testSet[x])
        neighbors = getNeighborsWithWeights(trainingSet, testSet[x], k)
        result = getRespWithWeights(neighbors)
	predictions.append(result)

    error = mse(predictions, testSet)

    print("MSE: " + repr(error) + "\n\n")
    
    plotResults(testSet, predictions, stockname)
