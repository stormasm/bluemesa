import os
import redis
import util

path = os.environ['BMTOP']
sp500_file = "/bluemesa/config/symbols/sp500.txt"
sp500_key = "symbol-set-sp500"

rc = redis.Redis(host='localhost', port=6379, db=0)

### Write data from a redis set to a txt file
def write_redis_set_to_file(filename,key):
    myset = util.redis_set_to_python_set(key)
    file = open(filename,"w")
    for member in myset:
        file.write(member)
        file.write('\n')
    file.close()

if __name__ == "__main__":
    filename = path + sp500_file
    write_redis_set_to_file(filename,sp500_key)
