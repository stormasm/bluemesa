import csv
import os

from os import listdir
from os.path import isfile, join

import redis

rc = redis.Redis(host='localhost', port=6379, db=0)

def get_symbol_from_filename(filename):
    file = os.path.basename(filename)
    tokens = file.split('-')
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
        next(funreader)
        for row in funreader:
            #print(row[0],row[2])
            write_data_to_redis_list(rediskey,row[0],row[2])

if __name__ == "__main__":
    path = os.environ['BMTOP']
    path = path + '/bluemesa/tmp'
    files = getfiles(path)
    for file in files:
        write_file_to_redis(file)
