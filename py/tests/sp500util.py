from sp500 import util

fb = util.get_symbol_name("fb")
#print(fb)
name = "Facebook Inc A"
assert(fb == name)
amzn = util.get_symbol_name("amzn")
#print(amzn)
name = "Amazon.com Inc"
assert(amzn == name)
print("sp500util test completed")
