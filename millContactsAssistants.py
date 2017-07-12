from csvreader import *

f = readCSV('millContacts.csv')

for i in enumerate(f):
    assistant = i[1][27]
    if len(assistant.split()) > 2:
        print(i[0], assistant)
