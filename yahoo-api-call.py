import csv
import json
import datetime
import pandas_datareader.data as web

def getData(filename, stockname, startdate, enddate):
    stock = web.DataReader(stockname, 'yahoo', startdate, enddate)
    print("done making network call")
    ass = [stock.index]
    stck_json = stock.to_json(orient="index", date_format='iso')
    stck_dates = json.loads(stck_json)

    plt.plot(stock["Adj Close"])
    plt.title("Stock movement of " + stockname)

    first_time = True
    with open(filename, 'wb') as pp:
        stockwriter = csv.writer(pp)
        stp = sorted(stck_dates.keys())
        for i in stp:
            new_format_date = i[:10]
            if first_time:
                first_time = False
                prev_closing = stck_dates[i]["Adj Close"]
                continue
            stockwriter.writerow([new_format_date] + [stck_dates[i]["Open"]] +  [stck_dates[i]["High"]] + [stck_dates[i]["Low"]]  +  [stck_dates[i]["Adj Close"]] + [change(stck_dates[i]["Adj Close"], prev_closing)])
            prev_closing = stck_dates[i]["Adj Close"]


def main():

    startdate = datetime.datetime(2002,1,1)
    enddate = datetime.date.today()

    getData('result.csv', 'yahoo', startdate, enddate)

main()
