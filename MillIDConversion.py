from csvreader import *
import csv

def convertMillIDs(filename):
    millID = readCSVasDict('MillIDConversion.csv')
    f = readCSV(filename)
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
