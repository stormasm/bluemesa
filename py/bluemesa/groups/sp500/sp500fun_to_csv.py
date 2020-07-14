import csv
import os
import pandas as pd
from pathlib import PurePath
import re

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

## https://docs.python.org/3/library/csv.html#csv.DictWriter

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

def write_schema_to_array(path):
    ary = []
    with open(path, newline='') as csvfile:
        funreader = csv.reader(csvfile, delimiter=',')
        # do not read the first line of the csv file
        next(funreader)
        for row in funreader:
            #print(row[0],row[2])
            ary.append(row[2])
    ary.insert(0,'symbol')
    return(ary)

if __name__ == "__main__":
    pathtop = os.environ['BMTOP']
#   path = path + '/equity-fun/sp500/data/20-07-12'
    path1 = pathtop + '/tmp/data'
    path2 = pathtop + '/bluemesa/config/schema-fun.csv'

    fieldnames = write_schema_to_array(path2)
    files = os.listdir(path1)

    with open('sp500fun.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(fieldnames)
        for file in files:
            filename = os.path.join(path1, file)
