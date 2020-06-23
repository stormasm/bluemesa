import os
from bluemesa.util import lineutil
import symboltable
import util

sdy_file = "/bluemesa/config/symbols/sdy.txt"
sdy_key = "symbol-set-sdy"
aristocrats_file = "/bluemesa/config/symbols/aristocrats.txt"
aristocrats_key = "symbol-set-aristocrats"

if __name__ == "__main__":
    path = os.environ['BMTOP']

    path_in  = path + sdy_file
    symbols = lineutil.get_lines_as_set(path_in)
    for symbol in symbols:
        symboltable.write_symbol_to_set(sdy_key,symbol)
    myset = util.redis_set_to_python_set(sdy_key)
    print("\n",myset)

    path_in  = path + aristocrats_file
    symbols = lineutil.get_lines_as_set(path_in)
    for symbol in symbols:
        symboltable.write_symbol_to_set(aristocrats_key,symbol)
    myset = util.redis_set_to_python_set(aristocrats_key)
    print("\n",myset)
