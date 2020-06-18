import json

# given a symbol get the company name
def get_symbol_name(symbol):
    with open('sp500n.json') as json_file:
        data = json.load(json_file)
        print(data[symbol])

# get all of the industry group symbols
def get_industry_group_symbols():
    symbols = set()
    with open('sp500.json') as json_file:
        dataList = json.load(json_file)
        for dict_item in dataList:
          for key in dict_item:
              symbols.add(key)
    return(symbols)

# get all of the symbols in the sp500
def get_all_symbols_sp500():
    symbols = set()
    with open('sp500.json') as json_file:
        dataList = json.load(json_file)
        for dict_item in dataList:
            for key in dict_item:
                #print(dict_item[key])
                #print("")
                for item in dict_item[key]:
                    print(item)
                    symbols.add(item)
    return(symbols)

# get all of the symbols in a particular industy group
def get_industry_group(symbol):
    with open('sp500.json') as json_file:
        dataList = json.load(json_file)
        for dict_item in dataList:
          for key in dict_item:
              if key == symbol:
                  print(key)
                  return(dict_item[key])

if __name__ == "__main__":
    get_symbol_name("fb")
    get_symbol_name("amzn")
    ig = get_industry_group("xlc")
    print(ig)
    symbols = get_industry_group_symbols()
    print(symbols)
    symbols = get_all_symbols_sp500()
    print(len(symbols))
