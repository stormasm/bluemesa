### Reads in the symbol file from a csv file instead of redis

import csv
import json
import os
import re

from os import listdir
from os.path import isfile, join

from bluemesa.redis import symboltable
from bluemesa.redis import util

path = os.environ['BMTOP']
symbol_filename = path + '/bluemesa/data/symbols.csv'
filename_in = path + '/bluemesa/data/topfun.json'
#filename_in = path + '/bluemesa/data/sp500fun.json'
#filename_in = path + '/bluemesa/data/mcapfun.json'
filename_out = path + '/bluemesa/tmp/fun/out/top.csv'

def get_symbol_name(symbol):
    with open(symbol_filename, newline='') as csvfile:
        symbolreader = csv.reader(csvfile, delimiter=',')
        symboldict = {};
        for row in symbolreader:
            symboldict[row[0]] = row[1]
        return(symboldict[symbol])

def remove_unwanted_chars(input):
    c = re.sub('[M,B,%]', '', input)
    return(c)

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
                fyield = remove_unwanted_chars(fyield)
                payout = dict[k][23]
                payout = remove_unwanted_chars(payout)
                operating = dict[k][48]
                operating = remove_unwanted_chars(operating)
                free = dict[k][49]
                free = remove_unwanted_chars(free)
                name = get_symbol_name(k)
                # when I get marketcap in redis add back in these 2 lines
                #mcap = util.redis_get_value("symbol-hash-mcap",k)
                #arr.append([idx,k,name,fyield,payout,mcap,operating,free])
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
