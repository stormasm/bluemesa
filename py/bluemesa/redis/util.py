import redis

rc = redis.Redis(host='localhost', port=6379, db=0)

def redis_set_to_python_set(key):
    members = set()
    rset = rc.smembers(key)
    for value in rset:
        value = value.decode("utf-8")
        members.add(value)
    return(members)

if __name__ == "__main__":
    rc.sadd('testset','red')
    rc.sadd('testset','yellow')
    rc.sadd('testset','green')
    myset = redis_set_to_python_set('testset')
    print(myset)
