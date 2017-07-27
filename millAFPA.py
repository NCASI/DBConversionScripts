from csvreader import *

f = readCSV('millafpa.csv')
t = open('millafpa.sql', 'w')
updatestr = "UPDATE dbo.MillInformation"
gostr = "GO\n"
total = 0
ctr = 0
for i in f:
    total +=1 
    if i[0] == '':
        continue
    
    value = "'"+i[0].strip()+"'"
    valstr = " SET MillInformation.AFPACode = " + value
    wherestr = " WHERE MillInformation.MillID = " + i[1] + "\n"
    updateSql = updatestr + valstr + wherestr
    t.write(updateSql)
    ctr += 1
t.write(gostr)
t.close()

print("=====================================")
print(ctr, "out of", total, "added.")
print("=====================================")
