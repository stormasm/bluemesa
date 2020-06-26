import json
import os
import pandas as pd
from pathlib import PurePath
import re


def get_symbol_from_filename1(filename):
    pp = PurePath(filename)
    # get the filename in the path
    p1 = pp.parts[-1]
    # get everything before the dot
    p2 = re.split("-",p1)[0]
    return(p2)



def get_symbol_from_filename(filename):
    pp = PurePath(filename)
    # get the filename in the path
    p1 = pp.parts[-1]
    # get everything before the dot
    p2 = re.split("\.",p1)[0]
    # get everything after holdings-
    p3 = re.split("holdings-",p2)[1]
    return(p3)

def get_dict1(filename):
    #print(filename)
    df = pd.read_csv(filename, sep=',')
    series = df['Value']
    values = series.values
    d = {}
    symbol = get_symbol_from_filename1(filename)
    print(symbol)
    d[symbol] = values
    return(d)

def get_dict(filename):
    df = pd.read_csv(filename, sep=',')
    series = df['Symbol']
    values = series.values
    # convert strings in array to lowercase
    vl = map(str.lower, values)
    d = {}
    symbol = get_symbol_from_filename1(filename)
    print(symbol)
    # convert the string array to a string tuple
    st = tuple(vl)
    d[symbol] = st
    return(d)

if __name__ == "__main__":
    path = os.environ['BMTOP']
    path = path + '/equity-fun/sp500/20-06-26'
    files = os.listdir(path)
    arr = []
    for file in files:
        filename = os.path.join(path, file)
        d = get_dict1(filename)
        arr.append(d)
    #myj = json.dumps(arr)
    #print(myj)
