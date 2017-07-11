from csvreader import *

f = readCSV('MillIDConversion.csv')
t = open('updateMillIDs.sql', 'w')
updatestr = "UPDATE dbo.MillInformation"
gostr = "GO\n"

for i in f:
    valstr = " SET MillInformation.MillID = " + i[0]
    wherestr = " WHERE MillInformation.PK_MillKey = " + i[1] + "\n"
    updateSql = updatestr + valstr + wherestr
    t.write(updateSql)
t.write(gostr)
t.close()
    
