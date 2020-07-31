import os
from bluemesa.edgar.pv3x import XBRLParser, GAAPSerializer

def parse(file):
    print("\nData for ",file)
    xbrl_parser = XBRLParser()
    xbrl = xbrl_parser.parse(open(file))
    #gaap_obj = xbrl_parser.parseGAAP(xbrl)
    gaap_obj = xbrl_parser.parseGAAP(xbrl, doc_date="20200331", context="current", ignore_errors=0)
    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)
    print(result)

if __name__ == "__main__":

    f1 = 'ubnt-20200331_htm.xml'

    path = os.environ['BMTOP']
    path = path + '/equity-data/edgar/'
    path = path + f1
    parse(path)
