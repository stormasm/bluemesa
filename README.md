This code requires that you have
[redis](http://redis.io)
installed on your system and that the redis server is up and running...

Set an environment variable **BMTOP**

```
cd into BMTOP
git clone this repository
```

```
cd bluemesa/py/yahoo_fin
python getfun.py
```

Now check and make sure the data written to **bluemesa/tmp** looks good.   

```
cd bluemesa/py/redis
python funlist.py
```

Now this data will be written to Redis...

Now run

```
python funschema.py
```

The schema data will now be loaded into Redis as well in the redis
key **schema-fun**
