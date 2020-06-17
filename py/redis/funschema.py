import csv
import os

from os import listdir
from os.path import isfile, join

import redis

rc = redis.Redis(host='localhost', port=6379, db=0)

def get_filename_from_path(path):
    file = os.path.basename(path)
    tokens = file.split('.')
    filename = tokens[0]
    return(filename)

def getfiles(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return(onlyfiles)

def write_data_to_redis_list(schema,index,data):
    rc.rpush(schema,data)

def write_schema_to_redis(path):
    rediskey = get_filename_from_path(path)
    print(rediskey)
    rc.delete(rediskey)
    with open(path, newline='') as csvfile:
        funreader = csv.reader(csvfile, delimiter=',')
        next(funreader)
        for row in funreader:
            print(row[0],row[2])
            write_data_to_redis_list(rediskey,row[0],row[2])

if __name__ == "__main__":
    path = os.environ['BMTOP']
    path = path + '/bluemesa/config/schema-fun.csv'
    write_schema_to_redis(path)
