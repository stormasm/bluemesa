import json
import os
import pandas as pd
from pathlib import PurePath
import re

def modify_array_values(input):
    arr = []
    for value in input:
        mytype = type(value)
        bool = isinstance(value,(float,tuple))
        #print(value,mytype,bool)
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
    p2 = re.split("-",p1)[0]
    return(p2)

def get_dict(filename):
    #print(filename)
    df = pd.read_csv(filename, sep=',')
    series = df['Value']
    values = series.values
    values = modify_array_values(values)
    d = {}
    symbol = get_symbol_from_filename(filename)
    st = tuple(values)
    d[symbol] = st
    return(d)

if __name__ == "__main__":
    path = os.environ['BMTOP']
    path = path + '/equity-fun/sp500/20-06-26'
    files = os.listdir(path)
    arr = []
    for file in files:
        filename = os.path.join(path, file)
        d = get_dict(filename)
        arr.append(d)
    myj = json.dumps(arr)
    print(myj)
