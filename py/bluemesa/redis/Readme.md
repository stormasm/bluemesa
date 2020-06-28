
##### funlist.py
Write a directory of yahoo_fin files that were generated via get_stats
to redis lists where each index in the list relates to fields in
the csv file.

##### funitems.py
Generates out a csv file with both the yield and payout
```
nu
open payout.csv | sort-by {yield, payout}
```
