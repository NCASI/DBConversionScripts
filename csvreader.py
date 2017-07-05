import csv
def readCSV(filename):
    dataArray = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            dataArray.append(row)
    csvfile.close()
    return dataArray
