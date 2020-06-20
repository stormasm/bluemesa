import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def redis_set_to_set(key):
    members = set()
    rset = r.smembers(key)
    for value in rset:
        value = value.decode("utf-8")
        members.add(value)
    return(members)

if __name__ == "__main__":
    r.sadd('testset','red')
    r.sadd('testset','yellow')
    r.sadd('testset','green')
    myset = redis_set_to_set('testset')
    print(myset)
