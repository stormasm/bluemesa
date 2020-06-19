import redis
from sp500 import util

rc = redis.Redis(host='localhost', port=6379, db=0)

def write_symbol_to_table(rediskey,symbol,name):
    rc.hset(rediskey,symbol,name)

if __name__ == "__main__":
    name = util.get_symbol_name("fb")
    write_symbol_to_table("symboltable","fb",name)
