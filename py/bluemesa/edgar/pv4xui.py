import os
from bluemesa.edgar.pv4x import XBRLParser, GAAPSerializer

def parse(file,doc_date):
    print("\nData for ",file)
    xbrl_parser = XBRLParser()
    xbrl = xbrl_parser.parse(open(file))

    gaap_obj = xbrl_parser.parseGAAP(xbrl, doc_date)

    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)
    print(result)

def get_doc_date(filename):
    date = filename.split("-")[2::][0]
    date = date.split("_")[0]
    return(date)

def getfiles(mypath):
    files = set()
    for file in os.listdir(mypath):
        if file.endswith(".xml"):
            files.add(os.path.join(mypath, file))
    return(files)

if __name__ == "__main__":
    path = os.environ['BMTOP']
    path = path + '/edgar-data/ubnt/'
    filenames = getfiles(path)
    for filename in filenames:
        doc_date = get_doc_date(filename)
        parse(filename,doc_date)
