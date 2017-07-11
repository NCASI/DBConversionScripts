"""
READCOORD.PY

Converts coordinates from format 4546210, -8759250 to
format 45°46'21.0" N, 87°59'25.0" W

INPUT: CSV of coordinates, extracted from original data file
OUTPUT: CSV of parsed coordinates

DEPENDENCIES: csvreader.py
"""

import os, sys

###YOUR FILENAME HERE###
filename = 'coordinates.csv'
########################

if not os.path.isfile(filename):
    print("ERROR: No such file as", "'" + filename + "'")
    sys.exit()

if not os.path.isfile('csvreader.py'):
    print("ERROR: Missing dependencies. Please make sure you have the following \nfiles in your directory:")
    print('\t -csvreader.py')
    sys.exit()


from csvreader import *
coordinates = readCSV()
t = open('parsedcoords1.csv','w')
for i in coordinates:
    if '' in i:
        string = '\n'
    else:
        rawlat = i[0]
        rawlong = i[1]
        rawlong = rawlong[1:]

        latstring = rawlat[:2] + '°' + rawlat[2:4] + "'" + rawlat[4:6] + '.' + rawlat[-1] + '" N'
        longstring = rawlong[:2] + '°' + rawlong[2:4] + "'" + rawlong[4:6] + '.' + rawlong[-1] + '" W'
        string = latstring + ', ' + longstring + '\n'
    t.write(string)
t.close()
