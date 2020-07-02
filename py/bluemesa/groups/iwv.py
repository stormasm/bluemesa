import json
import os
import pandas as pd

path_bmtop = os.environ['BMTOP']
iwv_csv_file = "/bluemesa/data/iwv.csv"

# Read the company name and symbol from a csv file
# and write the data out to json
def iwv_to_json():
    filename = path_bmtop + iwv_csv_file
    df = pd.read_csv(filename, sep=',')

    sseries = df['Ticker']
    svalues = sseries.values
    # convert strings in array to lowercase
    svlc = map(str.lower, svalues)
    symbols = tuple(svlc)

    nseries = df['Name']
    nvalues = nseries.values
    names = tuple(nvalues)
    d = {}
    for s, n in zip(symbols, names):
        d[s] = n
    myjson = json.dumps(d)
    print(myjson)

# Read the company name and symbol from a csv file
# and write it out to some other format
def iwv():
    filename = path_bmtop + iwv_csv_file
    df = pd.read_csv(filename, sep=',')
    tseries = df['Ticker']
    tickers = tseries.values
    nseries = df['Name']
    names = nseries.values
    # convert strings in array to lowercase
    tickers = map(str.lower, tickers)
    tickers = tuple(tickers)
    #names = map(str.lower,names)
    names = tuple(names)
    for i, name in enumerate(tickers):
        print(tickers[i],names[i])

# py iwv.py > iwvn.json
if __name__ == "__main__":
    #iwv_to_json()
    iwv()
