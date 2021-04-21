import json
import os
import pandas as pd
from pathlib import PurePath
import re

path = os.environ['BMTOP']
#path = path + '/equity-fun/sp500/data/20-07-12'
#path = path + '/equity-fun/mcap/mcap-g90'
path = path + '/bluemesa/tmp/fun/in/top'

def modify_array_values(input):
    arr = []
    for value in input:
        mytype = type(value)
        bool = isinstance(value,(float,tuple))
        if not bool:
            arr.append(value)
        else:
            arr.append("N/A")
    return(arr)

def get_symbol_from_filename(filename):
    pp = PurePath(filename)
    # get the filename in the path
    p1 = pp.parts[-1]
    # get everything before the dot
    p2 = re.split("-fun",p1)[0]
    return(p2)

def get_dict(filename):
    df = pd.read_csv(filename, sep=',')
    series = df['Value']
    values = series.values
    values = modify_array_values(values)
    d = {}
    symbol = get_symbol_from_filename(filename)
    st = tuple(values)
    d[symbol] = st
    return(d)

# Remember to remove the Readme in the directory
# py funjson.py > sp500fun.json
# py funjson.py > mcapfun.json
if __name__ == "__main__":
    files = os.listdir(path)
    arr = []
    for file in files:
        filename = os.path.join(path, file)
        d = get_dict(filename)
        arr.append(d)
    myj = json.dumps(arr)
    print(myj)
