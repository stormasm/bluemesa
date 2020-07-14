import os
import sqlite3

def init(filename):
    conn = sqlite3.connect(filename)
    return conn

def getCashFlow(filename):
    csq = init(filename)
    cursor = csq.cursor()
    t = ('ibm',)
    cursor.execute('SELECT * FROM sp500fun WHERE symbol=?', t)
    print(cursor.fetchone())

if __name__ == "__main__":
    path = os.environ['BMTOP']
    path = path + '/bluemesa/data/sp500fun.db'
    getCashFlow(path)
