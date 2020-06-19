import json
import os

# given a symbol get the company name
def get_symbol_name(symbol):

    path = os.environ['BMTOP']
    path = path + '/bluemesa/data/sp500n.json'
    with open(path) as json_file:
        data = json.load(json_file)
        return(data[symbol])

# get all of the industry group symbols
def get_industry_group_symbols():
    symbols = set()
    path = os.environ['BMTOP']
    path = path + '/bluemesa/data/sp500.json'
    with open(path) as json_file:
        dataList = json.load(json_file)
        for dict_item in dataList:
          for key in dict_item:
              symbols.add(key)
    return(symbols)

# get all of the symbols in the sp500
def get_all_symbols_sp500():
    symbols = set()
    path = os.environ['BMTOP']
    path = path + '/bluemesa/data/sp500.json'
    with open(path) as json_file:
        dataList = json.load(json_file)
        for dict_item in dataList:
            for key in dict_item:
                #print(dict_item[key])
                #print("")
                for item in dict_item[key]:
                    #print(item)
                    symbols.add(item)
    return(symbols)

# get all of the symbols in a particular industy group
def get_industry_group(symbol):
    path = os.environ['BMTOP']
    path = path + '/bluemesa/data/sp500.json'
    with open(path) as json_file:
        dataList = json.load(json_file)
        for dict_item in dataList:
          for key in dict_item:
              if key == symbol:
                  return(dict_item[key])

if __name__ == "__main__":
    get_symbol_name("fb")
    get_symbol_name("amzn")

    myig = "xlc"
    ig = get_industry_group(myig)
    print("\nThe symbols in the " + myig + " industry group")
    print(ig)

    print("\nThe Industry Group Symbols")
    symbols = get_industry_group_symbols()
    print(symbols)

    print("\nNumber of symbols in the sp500")
    symbols = get_all_symbols_sp500()
    print(len(symbols))
