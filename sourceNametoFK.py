from csvreader import *

#read in data
flowdata = readCSV('flowdata.csv')
sources = readCSV('sourcestbl.csv')

sourceNames = [i[1] for i in sources]   #get source names
flowcounter = 0                         #counter for total flow data info
foundcounter = 0                        #counter for correct matches
notFound = []                           #holds flows with no source
incorrectMatches = []                   #holds flows that were matched incorrectly

#iterate thru flowdata
for i in enumerate(flowdata):
    if i[0] == 0: continue  #skip the column header row
    flowsource = i[1][9]    #variable to hold the flowdata's source
    flowcounter += 1        

    #check if source exists in Sources Table
    if flowsource in sourceNames:    

        #change the flow data if the source names match
        if flowdata[i[0]][9] == sources[sourceNames.index(flowsource)][1]:
            flowdata[i[0]][9] = int(sources[sourceNames.index(flowsource)][0])
            foundcounter += 1

        #if sources names don't match, write to incorrectMatches
        else:
            incorrectMatches.append((flowsource, sources[sourceNames.index(flowsource)][1]))

    #if flow's source is not found, append to notFound
    else:
        notFound.append(flowsource)

#write to file
with open('flowdataWithSourceKeys.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in flowdata:
        csvwriter.writerow(i)

csvfile.close()
    
#print results
print("=================================")
print("Found",foundcounter,"out of",flowcounter,"matches.")

if notFound != []:
    print("The following sources were not found:")
    print(', '.join(notFound))

if incorrectMatches != []:
    print("The following sources were matched incorrectly:")
    print(', '.join(incorrectMatches))
print("=================================")
