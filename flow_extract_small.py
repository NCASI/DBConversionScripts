from csvreader import *
import csv

farray = []
ctr = 0
with open('NPDES_DMRS_FY2015.csv', 'r') as f:
    for line in f:
        line = line.split(',')
        if 'Flow' in line[13]:
            farray.append(line)
            ctr +=1
            print(ctr, "Found...")
with open('results.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in farray:
        csvwriter.writerow(i)

csvfile.close()
f.close()            
print(len(farray))
