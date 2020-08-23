
### Symbol Sets

**Bluemesa's** fundamental organizing principle is the symbol set.
Symbol sets are organized around indexes, etf's and guiding principles
including the
[SP500 Dividend Aristocrats](https://en.wikipedia.org/wiki/S%26P_500_Dividend_Aristocrats)

### Getting fundamental data

So one of the issues is grouping the data so you can compare
and contrast across different groups of companies or symbols.

Initially you have to get the data from somewhere...

For now I am getting the data from yahoo.
Eventually it will come from other places too like project edgar.

### Grouping data in many different ways

The fundamental grouping set is symbols.   
The symbol groups are in

### Redis sets with the key name delineating the group

  * symbol-set-aristocrats
  * symbol-set-sp500
  * symbol-set-sdy
  * symbol-set-pff

### symbol files with one line per symbol

### json files with each group as a set of symbols

Right now I am grouping data by indices such as the sp500
Grouping data by etfs such as pff and iwv which is the russell 3000 group
Grouping data by market cap which is data downloaded from green.

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

this takes in a symbol file which has one symbol per line
and writes out a csv file with the symbol and date.
the csv file contains the yahoo fundamental data.

getfun has a redis set symbol check in there where it checks
to see what files it has already downloaded...
reason this is here is because the program currently is not
bullet proof so it crashes sometimes.
so it has to be re-run until all the data is retrieved.
