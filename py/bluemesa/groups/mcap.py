import json
import os
import sys
import pandas as pd
from bluemesa.redis import util

path_bmtop = os.environ['BMTOP']
mcap_dir = "/equity-data/groups/mcap/data/200710/"

# Read the company name and symbol from a csv file
# and write the data out to json
def ishares_to_json(filename):
    filename = get_filename(symbol)
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
def ishares(symbol):
    filename = get_filename(symbol)
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
def ishares_to_redis_set(symbol):
    filename = get_filename(symbol)
    key = "symbol-set-" + symbol
    df = pd.read_csv(filename, sep=',')
    tseries = df['Ticker']
    tickers = tseries.values

    tickers = map(str.lower, tickers)
    tickers = tuple(tickers)
    for i, name in enumerate(tickers):
        util.redis_set_write(key,tickers[i])

def check_args(arg):
    group = {'pff','iwv'}
    return(arg in group)

def get_filename(symbol):
    filename = path_bmtop + ishares_dir + symbol + ".csv"
    return(filename)

def process(symbol):
    #ishares(symbol)
    #ishares_to_json(symbol)
    ishares_to_redis_set(symbol)

def arg_process():
    default = 'pff'
    num = len(sys.argv)
    if num > 1:
        arg = sys.argv[1]
    else:
        arg = default
    val = check_args(arg)
    if val:
        symbol = arg
    else:
        symbol = default
    return(symbol)

# py ishares.py > iwvn.json
if __name__ == "__main__":
    symbol = arg_process()
    process(symbol)
