import os

# This should return a set of lines
def get_lines_as_set(filename):
    myset = set()
    fp = open(filename, "r")
    for cnt, line in enumerate(fp):
        myline = line.strip()
        myset.add(myline)
    return(myset)

if __name__ == "__main__":
    path = os.environ['BMTOP']
    path_in  = path + '/bluemesa/config/symbols/sdy.txt'
    symbols = get_lines_as_set(path_in)
    print("The number of symbols = ",len(symbols))
