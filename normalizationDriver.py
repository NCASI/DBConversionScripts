"""
NORMALIZEDATA.PY

Driver program that performs data normalization for Mill Data tables.
Some tables will require further normalization.

INPUT: CSV of your table, taken from Access
OUTPUT: Normalized CSV to be imported to SQL Server
DEPENDENCIES: csvreader.py

INPUT PARAMETERS:

    sourceCol: Column in your input CSV that contains the source.
                For 1st column, enter 1; for 2nd, enter 2; etc

    filename: Filename of your input file. Enter the extension.
"""
from sourceNametoFK import *
from MillIDConversion import *
from csvreader import *
import csv

sourceCol = 5
filename = 'SludgeData.csv'

newFilename = convertMillIDs(filename)
convertSources(newFilename, sourceCol)
