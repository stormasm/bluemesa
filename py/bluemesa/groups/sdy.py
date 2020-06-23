import os
import pandas as pd

path_bmtop = os.environ['BMTOP']
sdy_csv_file = "/equity-data/groups/holdings-sdy.csv"

# Read the company name and symbol from a csv file
def sdy():
    filename = path_bmtop + sdy_csv_file
    df = pd.read_csv(filename, sep=',')
    tseries = df['Ticker']
    tickers = tseries.values
    nseries = df['Name']
    names = nseries.values
    # convert strings in array to lowercase
    tickers = map(str.lower, tickers)
    tickers = tuple(tickers)
    names = map(str.lower,names)
    names = tuple(names)
    for i, name in enumerate(tickers):
        print(tickers[i],names[i])

if __name__ == "__main__":
    sdy()
