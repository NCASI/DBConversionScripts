from csvreader import *

p = readCSV('temp_wood.csv')
t = open('insertwood.sql', 'w')
del p[0]
for i in p:
    wid = i[0]
    amt = i[1]
    thk = i[2]
    cf = i[3]
    units = i[4]
    insertstr = "INSERT INTO dbo.EHSSURVEY_WoodThickness ([WoodID],[Amount],[Thickness],[CF],[Units])\n"
    if thk == '':
        thk = "NULL"
    if amt == '':
        amt == "NULL"
    if cf == '':
        cf == "NULL"
    valstr = "VALUES (" + wid + "," + amt + "," + thk + "," + cf + ",'" + units + "')\n"

    gostr = "GO\n"

    sql = insertstr + valstr + gostr
    t.write(sql)
t.close()
