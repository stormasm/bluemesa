import os
from bluemesa.edgar.pv4x import XBRLParser, GAAPSerializer

def parse(file):
    print("\nData for ",file)
    xbrl_parser = XBRLParser()
    xbrl = xbrl_parser.parse(open(file))
#   gaap_obj = xbrl_parser.parseGAAP(xbrl, doc_date="20200331", context="current", ignore_errors=0)
#   gaap_obj = xbrl_parser.parseGAAP(xbrl, doc_date="20191231", context="current", ignore_errors=0)

    gaap_obj = xbrl_parser.parseGAAP(xbrl, doc_date="20200930")

    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)
    print(result)

if __name__ == "__main__":

    f1 = 'ubnt-20200930_htm.xml'
    f2 = 'ubnt-20200630_htm.xml'
    f3 = 'ubnt-20200331_htm.xml'
    f4 = 'ubnt-20191231_htm.xml'

    path = os.environ['BMTOP']
    path = path + '/edgar-data/ubnt/'
    path = path + f1
    parse(path)
