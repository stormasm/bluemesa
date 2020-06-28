import csv
import json
import os

from os import listdir
from os.path import isfile, join

import redis
import symboltable

rc = redis.Redis(host='localhost', port=6379, db=1)

def get_symbol_from_filename(filename):
    file = os.path.basename(filename)
    tokens = file.split('-fun')
    symbol = tokens[0]
    return(symbol)

def getfiles(mypath):
    files = set()
    for file in os.listdir(mypath):
        if file.endswith(".csv"):
            files.add(os.path.join(mypath, file))
    return(files)

def write_data_to_redis_list(symbol,index,data):
    rc.rpush(symbol,data)

def write_file_to_redis(filename):
    symbol = get_symbol_from_filename(filename)
    rediskey = symbol + "-fun"
    print(symbol)
    rc.delete(rediskey)
    with open(filename, newline='') as csvfile:
        funreader = csv.reader(csvfile, delimiter=',')
        # do not read the first line of the csv file
        next(funreader)
        for row in funreader:
            write_data_to_redis_list(rediskey,row[0],row[2])

def getSymbol(tsymbol):
    path = os.environ['BMTOP']
    filename = path + '/bluemesa/data/sp500fun.json'
    with open(filename) as json_file:
        data = json.load(json_file)
        numofitems = len(data)
        for i in range(numofitems):
            symbol = data[i]
            for k in symbol:
                if k == tsymbol:
                    value = symbol[k]
                    print(k,value[23])

def getPayoutRatio():
    path = os.environ['BMTOP']
    filename = path + '/bluemesa/data/sp500fun.json'
    arr = []
    with open(filename) as json_file:
        data = json.load(json_file)
        for idx,dict in enumerate(data):
            for k in dict:
                ## 19 is the forward dividend yield
                ## 23 is the payout ratio
                fyield = dict[k][19]
                payout = dict[k][23]
                name = symboltable.get_symbol_name(k)
                arr.append([idx,k,name,fyield,payout])
    return arr

def write_csv(data):
    path = os.environ['BMTOP']
    filename = path + '/bluemesa/tmp/fun/out/payout.csv'
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['index'] + ['symbol'] + ['name'] + ['yield'] + ['payout'])
        for row in data:
            csvwriter.writerow([row[0]] + [row[1]] + [row[2]] + [row[3]] + [row[4]])

if __name__ == "__main__":
    data = getPayoutRatio()
    write_csv(data)
    #getSymbol('t')
