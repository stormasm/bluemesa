
### Symbol Sets

**Bluemesa's** fundamental organizing principle is the symbol set.
Symbol sets are organized around equity indices, exchange traded funds (ETF) and guiding principles
including the
[SP500 Dividend Aristocrats](https://en.wikipedia.org/wiki/S%26P_500_Dividend_Aristocrats)

### Getting fundamental data

One of Bluemesa's core strengths is the API interface we use
to store and retrieve equity data.  Given a symbol set for
a group of stocks, one can then go out and retrieve fundamental
data.  For example purposes, this data comes from two sources.

  * [Yahoo Finance](https://finance.yahoo.com/)
  * [Edgar](https://www.sec.gov/edgar.shtml)

### Symbol set data representations

The fundamental grouping set is symbols. Symbols cans be stored in

  * Redis
  * Text files with one symbol per line
  * Json files with the symbol grouping name as the key and the symbols as the values

### Redis sets with the key name delineating the group

  * symbol-set-aristocrats
  * symbol-set-sp500
  * symbol-set-sdy
  * symbol-set-pff

### Text files with one line per symbol

### Json files

### Example Symbol Sets

  * Sp500
  * PFF
  * IWV which is the Russell 3000 group
  * Market cap groups

### To run the screens

```
screens/cashflow.py
```

The data is in the format of the sp500fun.json
which is a json file of fundamental data per symbol.
This is just a rollup of the individual yahoo csv files
combined into one json file.

### To grab fundamental data from yahoo

```
yahoo_fin/getfun.py
```

when you run getfun.py if no symbols get printed out
you have to remove the **symbol-check**-groupname
from redis.

this takes in a symbol file which has one symbol per line
and writes out a csv file with the symbol and date.
the csv file contains the yahoo fundamental data.

getfun has a redis set symbol check in there where it checks
to see what files it has already downloaded...
reason this is here is because the program currently is not
bullet proof so it crashes sometimes.
so it has to be re-run until all the data is retrieved.

### References
[Wikipedia Edgar](https://en.wikipedia.org/wiki/EDGAR)
