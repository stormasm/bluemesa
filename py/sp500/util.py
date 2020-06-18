import json

def get_symbol_dict(symbol):
    with open('sp500n.json') as json_file:
        data = json.load(json_file)
        print(data[symbol])

if __name__ == "__main__":
    get_symbol_dict("fb")
    get_symbol_dict("amzn")
