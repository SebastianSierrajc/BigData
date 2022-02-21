import sys
import re


ID = 'Transaction unique identifier'
PRICE = 'Price'
DATE = 'Date of Transfer'
TYPE = 'Property Type'
STATE = 'Old/New'
DURATION = 'Duration'
CITY = 'Town/City'
DISTRICT = 'District'
COUNTY = 'County'
PPD = 'PPDCategory Type'
RECORD = 'Record Status - monthly file only'

header = sys.stdin.readline()

for line in sys.stdin:
    words = line.strip('\n').split(',')
    date = words[2].split('-')
    year, month = date[0], date[1]
    print("{}\t{}".format(year, month))
