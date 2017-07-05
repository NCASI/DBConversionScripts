from csvreader import *
flowdata = readCSV('flowdata.csv')
sources = readCSV('flowdata.csv')
for i in flowdata:
    if i in sources:
        print(sources.index(i))
