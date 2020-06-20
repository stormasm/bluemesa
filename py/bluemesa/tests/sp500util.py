from bluemesa.sp500 import util
from bluemesa.redis import symboltable

### Getting data from sp500 json files

fb = util.get_symbol_name("fb")
#print(fb)
name = "Facebook Inc A"
assert(fb == name)
amzn = util.get_symbol_name("amzn")
#print(amzn)
name = "Amazon.com Inc"
assert(amzn == name)

### Getting data from redis

fb = symboltable.get_symbol_name("fb")
#print(fb)
name = "Facebook Inc A"
assert(fb == name)
amzn = symboltable.get_symbol_name("amzn")
#print(amzn)
name = "Amazon.com Inc"
assert(amzn == name)


print("sp500util tests completed")
