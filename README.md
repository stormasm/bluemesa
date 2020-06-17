This code requires that you have
[redis](http://redis.io)
installed on your system and that the redis server is up and running...

Set an environment variable **BMTOP**

```
cd into BMTOP
git clone this repository
```

```
cd bluemesa
python getfun.py
```

Now check and make sure the data written to **path_out** looks
good and then go ahead and set the same path_out directory in
redis/funlist.py and then run the program

```
python funlist.py
```

Now this data will be written to Redis...

Now run

```
python funschema.py
```

The schema data will now be loaded into Redis as well in the redis
key **schema-fun**
