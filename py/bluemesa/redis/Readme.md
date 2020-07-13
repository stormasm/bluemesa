
##### funschema.py
I map the yahoo_fin/getfun.py stats names from their names to my names
which I define in a file ./config/schema-fun.csv and write this schema
out to redis.

##### funlist.py
Write a directory of yahoo_fin/getfun.py output files that were generated via get_stats to redis lists where each index in the list relates to fields in
the csv file.

##### funitems.py
Generates out a csv file with both the yield and payout
```
nu
open payout.csv | sort-by {yield, payout}
```
