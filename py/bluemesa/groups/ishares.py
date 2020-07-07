import json
import os
import sys
import pandas as pd

path_bmtop = os.environ['BMTOP']
ishares_dir = "/equity-etf/data/ishares/"

# Read the company name and symbol from a csv file
# and write the data out to json
def ishares_to_json(filename):
    #filename = path_bmtop + iwv_csv_file
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
def ishares(filename):
    #filename = path_bmtop + iwv_csv_file
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

# Read the symbol from a csv file
# and write it out to a redis set
def ishares_to_redis_set(filename):
    #filename = path_bmtop + iwv_csv_file
    df = pd.read_csv(filename, sep=',')
    tseries = df['Ticker']
    tickers = tseries.values

    tickers = map(str.lower, tickers)
    tickers = tuple(tickers)
    for i, name in enumerate(tickers):
        print(tickers[i])

def check_args(arg):
    group = {'pff','iwv'}
    return(arg in group)

def get_filename(symbol):
    filename = path_bmtop + ishares_dir + symbol + ".csv"
    return(filename)

def process(filename):
    #ishares(filename)
    #ishares_to_json(filename)
    ishares_to_redis_set(filename)

def arg_process():
    default = 'iwv'
    num = len(sys.argv)
    if num > 1:
        arg = sys.argv[1]
    else:
        arg = default
    val = check_args(arg)
    if val:
        filename = get_filename(arg)
    else:
        filename = get_filename(default)
    return(filename)

# py ishares.py > iwvn.json
if __name__ == "__main__":
    filename = arg_process()
    process(filename)
