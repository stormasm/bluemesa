import datetime
import os
from yahoo_fin.stock_info import get_stats
from bluemesa.util import lineutil
from bluemesa.redis import util

def get_day():
    x = datetime.datetime.now()
    y = x.strftime("%y-%m-%d")
    return y

def build_file_name(symbol):
    day = get_day()
    filename = f"{symbol}-fun-{day}.csv"
    return(filename)

def process(symbols,path,key):
    for symbol in symbols:
        print(symbol)
        filename = build_file_name(symbol)
        bool = util.redis_set_read(key,symbol)
        if not bool:
            data = get_stats(symbol)
            out_file = path + filename
            data.to_csv(out_file)
            util.redis_set_write(key,symbol)

if __name__ == "__main__":
    path = os.environ['BMTOP']
    path_in  = path + '/bluemesa/config/symbols/sp500.txt'
    path_out = path + '/bluemesa/tmp/fun/in/'
    symbols = lineutil.get_lines_as_set(path_in)
    process(symbols,path_out,"symbol-check")

# The variable symbols is always a Python set which is nice
# because then we will not get any duplication of data
# symbols = {"ui","psa","ip","t"}
# symbols.add("nly")
