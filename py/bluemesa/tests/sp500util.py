from bluemesa.sp500 import util
from bluemesa.redis import symboltable

name_fb = "Facebook Inc A"
name_amzn = "Amazon.com Inc"

### Getting data from sp500 json files
fb = util.get_symbol_name("fb")
assert(fb == name_fb)

amzn = util.get_symbol_name("amzn")
assert(amzn == name_amzn)

### Getting data from redis

fb = symboltable.get_symbol_name("fb")
assert(fb == name_fb)

amzn = symboltable.get_symbol_name("amzn")
assert(amzn == name_amzn)

print("sp500util tests completed")
