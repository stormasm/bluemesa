import csv

from os import listdir
from os.path import isfile, join

import redis

rc = redis.Redis(host='localhost', port=6379, db=0)

def getfiles(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return(onlyfiles)

def write_file_to_redis(filename):
    with open(filename, newline='') as csvfile:
        funreader = csv.reader(csvfile, delimiter=',')
        next(funreader)
        for row in funreader:
            print(row[0],row[2])

if __name__ == "__main__":
    path = '/j/tmp32/bluemesa/tmp'
    myfiles = getfiles(path)
    for filename in myfiles:
        file = path + '/' + filename
        write_file_to_redis(file)
