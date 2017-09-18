import datetime
from model import predictFor

def main():

    predictFor(5, 'amtd.csv', 'AMTD', datetime.datetime(2012,6,23), datetime.date.today(), 1, 0.67)
    predictFor(5, 'disney.csv', 'DIS', datetime.datetime(2002,6,23), datetime.date.today(), 1, 0.67)
    predictFor(5, 'twtr.csv', 'TWTR', datetime.datetime(2013,6,23), datetime.date.today(), 1, 0.67)
    

main()
