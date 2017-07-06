from csvreader import *
import csv

def convertMillIDs(filename):
    millID = readCSVasDict('MillIDConversion.csv')
    f = readCSV(filename)
    if f is None or millID is None:
        print("Error reading in files!")
        return
    changectr = 0
    totalctr = 0
    for i in enumerate(f):
        totalctr += 1
        if i[0] == 0: continue
        oldID = i[1][0]
        newID = millID[oldID][0]
        if newID != oldID:
            #print(oldID, "!=", newID)
            i[1][0] = newID
            changectr += 1
    #write to file
    newfile = 'NEW_'+filename
    with open(newfile, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in f:
            csvwriter.writerow(i)

    csvfile.close()
    #print results
    print("=================================")
    print("Changed",changectr,"out of",totalctr,"entries.")
    print("=================================")


def generateSQLforMillInfo():
    f = readCSV('MillIDConversion.csv')
    t = open('correctMillIDs.sql', 'w')
    changectr = 0
    del f[0]
    for i in f:
        old = int(i[0])
        new = int(i[1])
        if old != new:
            sql = "UPDATE dbo.MillInformation SET MillID = " + str(old) + " WHERE MillID = " + str(new) + "\n"
            t.write(sql)
            changectr += 1
    print(changectr, " rows changed.")
    t.close()
generateSQLforMillInfo()
