import csv
import json
import os

from os import listdir
from os.path import isfile, join

from bluemesa.redis import symboltable

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
