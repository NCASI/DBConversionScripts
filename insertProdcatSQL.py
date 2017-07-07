from csvreader import *

p = readCSV('prodcats.csv')
t = open('insertprodcatsql.sql', 'w')
del p[0]
for i in p:
    factype = i[0]
    prodtype = i[1]
    cat = i[2]
    desc = i[3]
    epa = i[4]
    fs = i[5]
    print(epa)
    insertstr = "INSERT INTO dbo.NCASIProdCat ([FacType],[ProdType],[Category],[ProdCatDescription],[FK_EPASubcatID],[FiberSource])\n"
    if epa != '':
        valstr = "VALUES ('" + factype + "','" + prodtype + "','" + cat + "','" + desc + "','" + epa + "','" + fs + "')\n"
    if epa == '':
        valstr = "VALUES ('" + factype + "','" + prodtype + "','" + cat + "','" + desc + "', " + "NULL" + " ,'" + fs + "')\n"

    gostr = "GO\n"

    sql = insertstr + valstr + gostr
    t.write(sql)
t.close()
