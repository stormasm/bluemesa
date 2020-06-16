import datetime
from yahoo_fin.stock_info import get_stats

# This should return a set of symbols
def get_symbols(filename):
    myset = set()
    fp = open(filename, "r")
    for cnt, line in enumerate(fp):
        symbol = line.strip()
        myset.add(symbol)
    return(myset)

def get_day():
    x = datetime.datetime.now()
    y = x.strftime("%y-%m-%d")
    return y

def build_file_name(symbol):
    day = get_day()
    filename = f"{symbol}-fun-{day}.csv"
    return(filename)

def process(symbols,path):
    for symbol in symbols:
        print(symbol)
        filename = build_file_name(symbol)
        data = get_stats(symbol)
        out_file = path + filename
        data.to_csv(out_file)

if __name__ == "__main__":
    path_in  = '/j/tmp32/equity-data/symbols/top.txt'
    path_out = '/j/tmp32/bluemesa/tmp/'
    symbols = get_symbols(path_in)
    process(symbols,path_out)

# This is a Python set which is nice because we can not
# get any duplication of data...
# symbols = {"ui","psa","ip","t"}
# symbols.add("nly")
