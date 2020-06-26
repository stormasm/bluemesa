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

def redis_set_write(key,member):
    rc.sadd(key,member)

def redis_set_read(key,member):
    value = rc.sismember(key,member)
    return(value)

def redis_delete(key):
    rc.delete(key)

if __name__ == "__main__":
    k = "mykey"
    redis_set_write(k,"or")
    redis_set_write(k,"ca")
    redis_set_write(k,"tx")
    val = redis_set_to_python_set(k)
    ok1 = "or" in val
    ok2 = "ca" in val
    ok3 = "tx" in val
    ok4 = "nm" in val
    assert ok1 == True
    assert ok2 == True
    assert ok3 == True
    assert ok4 == False
    val = redis_set_read(k,"or")
    assert val == True
    val = redis_set_read(k,"nm")
    assert val == False
    val = rc.exists(k)
    assert val == True
    redis_delete(k)
    val = rc.exists(k)
    assert val == False
