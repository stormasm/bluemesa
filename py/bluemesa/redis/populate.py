import os
from bluemesa.util import lineutil
import symboltable
import util

path = os.environ['BMTOP']
sdy_file = "/bluemesa/config/symbols/sdy.txt"
sdy_key = "symbol-set-sdy"
aristocrats_file = "/bluemesa/config/symbols/aristocrats.txt"
aristocrats_key = "symbol-set-aristocrats"
iwv_file = "/bluemesa/config/symbols/iwv.txt"
iwv_key = "symbol-set-iwv"

def sdy():
    path_in  = path + sdy_file
    symbols = lineutil.get_lines_as_set(path_in)
    for symbol in symbols:
        symboltable.write_symbol_to_set(sdy_key,symbol)
    myset = util.redis_set_to_python_set(sdy_key)
    print("\n",myset)

def aristocrats():
    path_in  = path + aristocrats_file
    symbols = lineutil.get_lines_as_set(path_in)
    for symbol in symbols:
        symboltable.write_symbol_to_set(aristocrats_key,symbol)
    myset = util.redis_set_to_python_set(aristocrats_key)
    print("\n",myset)

def iwv():
    path_in  = path + iwv_file
    symbols = lineutil.get_lines_as_set(path_in)
    for symbol in symbols:
        symboltable.write_symbol_to_set(iwv_key,symbol)
    myset = util.redis_set_to_python_set(iwv_key)
    print("\n",myset)

if __name__ == "__main__":
    sdy()
    aristocrats()
    iwv()
