"""
This script takes in a CSV file and changes source names
to foreign keys for import into the Mill Data database in
SQL server.


INPUT: CSV file of table from Access
OUTPUT: CSV file of table to be imported to SQL Server
DEPENDENCIES: sourcestbl.csv
"""

from csvreader import *

#read in data
flowdata = readCSV('prodcats.csv')
sources = readCSV('sourcestbl.csv')

sourceNames = [i[1] for i in sources]   #get source names
flowcounter = 0                         #counter for total flow data info
foundcounter = 0                        #counter for correct matches
notFound = []                           #holds flows with no source
incorrectMatches = []                   #holds flows that were matched incorrectly
emptyVals = 0
#iterate thru flowdata
for i in enumerate(flowdata):
    if i[0] == 0: continue  #skip the column header row
    flowsource = i[1][5]    #variable to hold the flowdata's source
    flowcounter += 1        

    #check if source exists in Sources Table
    if flowsource in sourceNames:    

        #change the flow data if the source names match
        if flowdata[i[0]][5] == sources[sourceNames.index(flowsource)][1]:
            flowdata[i[0]][5] = int(sources[sourceNames.index(flowsource)][0])
            foundcounter += 1

        #if sources names don't match, write to incorrectMatches
        else:
            incorrectMatches.append((flowsource, sources[sourceNames.index(flowsource)][1]))

    #if flow's source is not found, append to notFound
    elif flowsource.strip() != '':
        notFound.append(flowsource)
    else:
        emptyVals += 1

#write to file
with open('prodcatsWithSourceKeys.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in flowdata:
        csvwriter.writerow(i)

csvfile.close()
    
#print results
print("=============================================")
print("Found",foundcounter,"out of",flowcounter,"matches.")

    
if emptyVals > 0:
    print("There were", emptyVals, "empty source values.")
    
if notFound != []:
    print("The following sources were not found:")
    print(', '.join(notFound))
    
if incorrectMatches != []:
    print("The following sources were matched incorrectly:")
    print(', '.join(incorrectMatches))
print("=============================================")
