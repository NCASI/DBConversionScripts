"""
This script takes in a CSV file of MillData.Production
and changes "Prod_Type" and "Category" fields to a FK
referencing the NCASIProdCat table.


INPUT: CSV file of MillData.Production, MillData.ProdCats
OUTPUT: CSV file of table to be imported to SQL Server
DEPENDENCIES: sourcestbl.csv
"""
from csvreader import *
from collections import defaultdict
import csv
prodData = readCSV('prodDataWithSourceKeys.csv')
reftable = readCSV('prodcatswithid_NEW.csv')
refdict = defaultdict(int)
matchesfound = 0
total = 0
mismatches = []
for i in enumerate(reftable):
    if i[0] == 0: continue
    #print(i[1])
    key = i[1][1] +","+ i[1][2]
    refdict[key] = int(i[1][0])
#(len(prodData))
for i in enumerate(prodData):
    #(prodData[i[0]])
    
    if i[0] == 0: continue
    total += 1
    key = i[1][1] + "," + i[1][2]
    if key in refdict:
        prodData[i[0]][3] = refdict[key]
        matchesfound += 1
    else:
        mismatches.append(key)
        prodData[i[0]][3] = ''

if len(mismatches) > 0:
    t = open('prodcatreport.csv', 'w')
    x = list(set(mismatches))
    s = open('insertmissingprodcats.sql', 'w')
    insertstr = "INSERT INTO dbo.NCASIProdCat ([ProdType],[Category],[Comment])\n"
    gostr = "GO\n"
    for i in x:
        w = i.split(",")
        t.write(i + ','+str(mismatches.count(i)) + '\n')
        valstr = "VALUES ('" + w[0] + "','" + w[1] + "','Retained for historical reasons')\n"
        sql = insertstr + valstr + gostr
        s.write(sql)
    t.close()
    s.close()
    
    
     

with open('prodDataWithProdcatIDs.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in prodData:
            del i[1]
            del i[1]
            csvwriter.writerow(i)

csvfile.close()

#print results
print("=================================")
print("Changed",matchesfound,"out of",total,"entries.")

if len(mismatches) > 0:
    print(len(mismatches), " keys were not found:")
    print(mismatches)
    print("Please run insertmissingprodcats.sql, \n \
            download the table, and run this script again.")
print("=================================")


