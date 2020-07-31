import os
from bluemesa.edgar.pv3x import XBRLParser, GAAPSerializer

def parse(file):
    print("\nData for ",file)
    xbrl_parser = XBRLParser()
    xbrl = xbrl_parser.parse(open(file))
#   gaap_obj = xbrl_parser.parseGAAP(xbrl, doc_date="20200331", context="current", ignore_errors=0)
    gaap_obj = xbrl_parser.parseGAAP(xbrl, doc_date="20191231", context="current", ignore_errors=0)
    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)
    print(result)

if __name__ == "__main__":

    f1 = 'ubnt-20200331_htm.xml'
    f2 = 'ubnt-20191231_htm.xml'

    path = os.environ['BMTOP']
    path = path + '/equity-data/edgar/'
    path = path + f2
    parse(path)
