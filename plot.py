import matplotlib.pyplot as plt   
import datetime



def plotResults(testSet, predictions, stockname):
    plt.figure("Stock price prediction using KNN Regressor")
    plt.title("Prediction vs Actual Trend of " + stockname)
    plt.legend(loc="best")
    row = []
    col = []
    for x in range(len(testSet)):
        new_date = datetime.datetime.strptime(testSet[x][0], "%Y-%m-%d").date()
        row.append(new_date)
        col.append(predictions[x])
    predicted_plt, = plt.plot(row, col, 'r', label='Predicted')

    plt.legend(handles=[predicted_plt])

    row = []
    col = []
    for x in range(len(testSet)):
        new_date = datetime.datetime.strptime(testSet[x][0], "%Y-%m-%d").date()
        row.append(new_date)
        col.append(testSet[x][-1])
    actual_plt, = plt.plot(row, col, 'b', label='Actual')

    plt.legend(handles=[predicted_plt, actual_plt])


    plt.show()