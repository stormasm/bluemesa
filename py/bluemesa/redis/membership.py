import os
import symboltable
import util

def sdy_sp500():
    set1 = util.redis_set_to_python_set("symbol-set-sdy")
    set2 = util.redis_set_to_python_set("symbol-set-sp500")

    intersection = set1.intersection(set2)
    print("\nThese symbols are in the sp500")
    print(intersection)
    print(len(intersection))

    difference = set1.difference(intersection)
    print("\nThese symbols are not in the sp500")
    print(difference)
    print(len(difference))

    print("\nThe total number of symbols in both sets")
    print(len(set1))

def aristocrats_sdy():
    set1 = util.redis_set_to_python_set("symbol-set-aristocrats")
    set2 = util.redis_set_to_python_set("symbol-set-sdy")

    intersection = set1.intersection(set2)
    print("\nThese symbols are in the sdy")
    print(intersection)
    print(len(intersection))

    difference = set1.difference(intersection)
    print("\nThese symbols are not in the sdy")
    print(difference)
    print(len(difference))

    print("\nThe total number of symbols in both sets")
    print(len(set1))


if __name__ == "__main__":
    #sdy_sp500()
    aristocrats_sdy()
