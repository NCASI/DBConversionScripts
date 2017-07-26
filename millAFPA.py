from csvreader import *

f = readCSV('millafpa.csv')
t = open('millafpa.sql', 'w')
updatestr = "UPDATE dbo.MillInformation"
gostr = "GO\n"

for i in f:

    valstr = " SET MillInformation.AFPACode = " + i[0]
    wherestr = " WHERE MillInformation.MillID = " + i[1] + "\n"
    updateSql = updatestr + valstr + wherestr
    t.write(updateSql)

t.write(gostr)
t.close()


