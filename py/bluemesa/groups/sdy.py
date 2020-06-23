import os
import pandas as pd

path_bmtop = os.environ['BMTOP']
sdy_csv_file = "/equity-data/groups/holdings-sdy.csv"

def sdy():
    filename = path_bmtop + sdy_csv_file
    df = pd.read_csv(filename, sep=',')
    series = df['Ticker']
    values = series.values
    # convert strings in array to lowercase
    vl = map(str.lower, values)
    print(tuple(vl))

def get_dict(filename):
    df = pd.read_csv(filename, sep=',')
    series = df['Symbol']
    values = series.values
    # convert strings in array to lowercase
    vl = map(str.lower, values)
    d = {}
    symbol = get_symbol_from_filename(filename)
    # convert the string array to a string tuple
    st = tuple(vl)
    d[symbol] = st
    return(d)

if __name__ == "__main__":
    sdy()
