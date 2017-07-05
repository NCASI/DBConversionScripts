from csvreader import *
coordinates = readCSV('coordinates.csv')
t = open('parsedcoords1.csv','w')
for i in coordinates:
    if '' not in i:
        rawlat = i[0]
        rawlong = i[1]
        rawlong = rawlong[1:]

        latstring = rawlat[:2] + '°' + rawlat[2:4] + "'" + rawlat[4:6] + '.' + rawlat[-1] + '" N'
        longstring = rawlong[:2] + '°' + rawlong[2:4] + "'" + rawlong[4:6] + '.' + rawlong[-1] + '" W'
        string = latstring + ', ' + longstring + '\n'
        t.write(string)
t.close()
