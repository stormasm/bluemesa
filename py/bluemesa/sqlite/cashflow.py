import os
import sqlite3

def init(filename):
    conn = sqlite3.connect(filename)
    return conn

def getCashFlow(filename, symbol):
    conn = init(filename)
    cursor = conn.cursor()
    t = (symbol,)
    cursor.execute('SELECT "operating-cash-flow", "levered-free-cash-flow" FROM sp500fun WHERE symbol=?', t)
    resultset = cursor.fetchone()
    return(resultset)

if __name__ == "__main__":
    path = os.environ['BMTOP']
    path = path + '/bluemesa/data/sp500fun.db'
    resultset = getCashFlow(path,'ibm')
    print(resultset)
