
This code requires that you have
[redis](redis.io)
installed on your
system and that the redis server is up and running...

Create a symbol file with one symbol per line...

```
aapl
amzn
nflx
```

Go to the yahoo_fin directory and set the directories:
* path_in
* path_out
in the file **getfun.py** and then run the program

```
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

The schema data will not be loaded into Redis as well...
