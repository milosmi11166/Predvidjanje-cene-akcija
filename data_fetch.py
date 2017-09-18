import csv
import random
import json
import pandas_datareader.data as web

def getData(filename, stockname, startdate, enddate):
    stock = web.DataReader(stockname, 'yahoo', startdate, enddate)
    print("Ok!")
    stck_json = stock.to_json(orient="index", date_format='iso')
    stck_dates = json.loads(stck_json)

    with open(filename, 'wb') as pp:
        stockwriter = csv.writer(pp)
        stp = sorted(stck_dates.keys())
        for i in stp:
            new_format_date = i[:10]
            stockwriter.writerow([new_format_date] + [stck_dates[i]["Open"]] +  [stck_dates[i]["High"]] + [stck_dates[i]["Low"]]  +  [stck_dates[i]["Adj Close"]] )



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
