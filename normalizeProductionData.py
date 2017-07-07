"""
This script takes in a CSV file of MillData.Production
and changes "Prod_Type" and "Category" fields to a FK
referencing the NCASIProdCat table.


INPUT: CSV file of MillData.Production, MillData.ProdCats
OUTPUT: CSV file of table to be imported to SQL Server
DEPENDENCIES: sourcestbl.csv
"""
from csvreader import *

prodData = readCSV('prodDataWithSourceKeys.csv')
reftable = readCSV('prodcatswithid.csv')
refdict = {}
for i in enumerate(reftable):
    if i[0] == 0: continue
    refdict[i[1][1:]] = i[1][0]
print(refdict)
#for i in enumerate(prodData):
#    if i[0] == 0: continue
    

