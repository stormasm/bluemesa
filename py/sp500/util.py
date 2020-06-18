import json

def get_symbol_dict(symbol):
    with open('sp500n.json') as json_file:
        data = json.load(json_file)
        print(data[symbol])

def get_industry_group(symbol):
    with open('sp500.json') as json_file:
        dataList = json.load(json_file)
        for dict_item in dataList:
          for key in dict_item:
            print(key)
            #print(dict_item[key])

if __name__ == "__main__":
    get_symbol_dict("fb")
    get_symbol_dict("amzn")
    get_industry_group("xle")
