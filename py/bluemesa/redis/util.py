# Note that these are generic functions which do not have
# anything to do with bluemesa but could be used generically
# across any project that uses python and redis

import redis

rc = redis.Redis(host='localhost', port=6379, db=0)

def redis_set_to_python_set(key):
    members = set()
    rset = rc.smembers(key)
    for value in rset:
        value = value.decode("utf-8")
        members.add(value)
    return(members)
