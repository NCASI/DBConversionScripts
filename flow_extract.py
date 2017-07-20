from csvreader import *
import csv

farray = []
ctr = 0
total = 0
with open('NPDES_DMRS_FY2015.csv', 'r') as f:
    with open('results.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for line in f:
            total += 1
            line = line.split(',')
            if 'Flow' in line[13]:
                csvwriter.writerow(line)
                ctr +=1
                print(ctr,"/", total)

csvfile.close()
f.close()            
print(len(farray))
