
For a high level overview of the concepts see the document

 * [workflow](./doc/workflow.md)

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
python funschema.py
```

Now bring up a redis-client and run the command

```
keys *
```

To see how all of your data was written to redis.
