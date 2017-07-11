from csvreader import *
import csv

raw = readCSV('codischarger.csv')
t = open('codischSorted.csv', 'w')
sortedData = []
for i in enumerate(raw):
    if i[0] == 0: continue
    temp = [int(i[1][0]),int(i[1][1])]
    sortedData.append(sorted(temp))

sortedData = list(set(map(tuple,sortedData)))

for i in sortedData:
    tstr = str(i[0]) + "," + str(i[1]) + "\n"
    t.write(tstr)
t.close()
    
    
