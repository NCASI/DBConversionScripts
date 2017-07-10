"""
NORMALIZATIONDRIVER.PY

Driver program that performs data normalization for Mill Data tables.
Some tables will require further normalization.

INPUT: CSV of your table, taken from Access
OUTPUT: Normalized CSV to be imported to SQL Server
DEPENDENCIES: csvreader.py, sourceNametoFK.py, MillIDConversion.py,
                MillIDConversion.csv, sourcestbl.csv

INPUT PARAMETERS:

    sourceCol: Column in your input CSV that contains the source.
                For 1st column, enter 1; for 2nd, enter 2; etc

    filename: Filename of your input file. Enter the extension.
"""

#MAKE YOUR CHANGES HERE
sourceCol = 5
filename = 'siccodes.csv'
#########################

import sys, os

#handle dependencies
if (not os.path.isfile('MillIDConversion.csv') or
    not os.path.isfile('sourcestbl.csv') or
    not os.path.isfile('sourceNametoFK.py') or
    not os.path.isfile('MillIDConversion.py')):
    print("ERROR: Missing dependencies. Please make sure you have the following \nfiles in your directory:")
    print('\t -csvreader.py\n\t -sourceNametoFK.py\n\t -MillIDConversion.py\n\t -MillIDConversion.csv\n\t -sourcestbl.csv')
    sys.exit()

if not os.path.isfile(filename):
    print("ERROR: No such file as", "'" + filename + "'")
    sys.exit()

#import dependencies
from sourceNametoFK import *
from MillIDConversion import *
from csvreader import *

newFile = convertMillIDs(filename)
#newFile = convertSources(millIDConverted, sourceCol)
#print("\n **** Your target file is: ", newFile, " ****")
