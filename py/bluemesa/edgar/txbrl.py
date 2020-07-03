import os
from xbrl import XBRLParser, GAAP, GAAPSerializer

def getfiles(mypath):
    files = set()
    for file in os.listdir(mypath):
        if file.endswith(".xml"):
            files.add(os.path.join(mypath, file))
    return(files)

def parse(file):
    xbrl_parser = XBRLParser()
    xbrl = xbrl_parser.parse(open(file))

if __name__ == "__main__":
    path = os.environ['BMTOP']
    path = path + '/equity-data/edgar'
    files = getfiles(path)
    for file in files:
        parse(file)
