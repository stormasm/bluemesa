import redis
from bluemesa.sp500 import util

rc = redis.Redis(host='localhost', port=6379, db=0)

def write_symbol_to_set(rediskey,symbol):
    rc.sadd(rediskey,symbol)

def write_symbol_to_table(rediskey,symbol,name):
    rc.hset(rediskey,symbol,name)

def get_symbol_name(symbol):
    name = rc.hget("symboltable",symbol)
    name = name.decode("utf-8")
    return(name)

if __name__ == "__main__":
    name = util.get_symbol_name("fb")
    print(name)
    write_symbol_to_table("symboltable","fb",name)
    sp500 = util.get_all_symbols_sp500()
    for symbol in sp500:
        print(symbol)
        name = util.get_symbol_name(symbol)
        write_symbol_to_table("symboltable",symbol,name)
        write_symbol_to_set("symbol-set-sp500",symbol)
