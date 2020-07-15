import json
import os
import sys
import pandas as pd
from bluemesa.redis import util

path_bmtop = os.environ['BMTOP']
mcap_dir = "/equity-data/groups/mcap/data/200710/"

mcapfile = {
  "g90": "mcap90up",
  "g50": "mcap50-90",
  "g30": "mcap30-50"
}

# Read the company name and symbol from a csv file
# and write the data out to json
def mcap_to_json(filename):
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
def mcap(symbol):
    filename = get_filename(symbol)
    df = pd.read_csv(filename, sep=',')
    tseries = df['Symbol']
    tickers = tseries.values
    nseries = df['Market Capitalization']
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
def mcap_to_redis_set(symbol):
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
    group = {'g90','g50','g30'}
    return(arg in group)

def get_filename(symbol):
    symbol = mcapfile[symbol]
    filename = path_bmtop + mcap_dir + symbol + ".csv"
    return(filename)

def process(symbol):
    mcap(symbol)
    #mcap_to_json(symbol)
    #mcap_to_redis_set(symbol)

def arg_process():
    default = 'g90'
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

# py mcap.py > iwvn.json
if __name__ == "__main__":
    symbol = arg_process()
    process(symbol)
