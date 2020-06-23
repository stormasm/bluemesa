import os
from bluemesa.util import symbol
from bluemesa.redis import symboltable

if __name__ == "__main__":
    path = os.environ['BMTOP']
    path_in  = path + '/bluemesa/config/symbols/sdy.txt'
    symbols = symbol.get_symbols(path_in)
    for symbol in symbols:
        symboltable.write_symbol_to_set("symbol-set-sdy",symbol)
