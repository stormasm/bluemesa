import csv
import json
import os

from os import listdir
from os.path import isfile, join

from bluemesa.redis import symboltable

path = os.environ['BMTOP']
#filename_in = path + '/bluemesa/data/sp500fun.json'
filename_in = path + '/bluemesa/data/mcapfun.json'
filename_out = path + '/bluemesa/tmp/fun/out/cashflow.csv'

def getCashFlow():
    arr = []
    with open(filename_in) as json_file:
        data = json.load(json_file)
        for idx,dict in enumerate(data):
            for k in dict:
                ## 19 is the forward dividend yield
                ## 23 is the payout ratio
                ## 48 is the operating cash flow
                ## 49 is the levered free cash flow
                fyield = dict[k][19]
                payout = dict[k][23]
                operating = dict[k][48]
                free = dict[k][49]
                name = symboltable.get_symbol_name(k)
                arr.append([idx,k,name,fyield,payout,operating,free])
    return arr

def write_csv(data):
    with open(filename_out, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['index'] + ['symbol'] + ['name'] + ['yield'] + ['payout'] + ['operating'] + ['levered'])
        for row in data:
            csvwriter.writerow([row[0]] + [row[1]] + [row[2]] + [row[3]] + [row[4]] + [row[5]] + [row[6]])

if __name__ == "__main__":
    data = getCashFlow()
    write_csv(data)
