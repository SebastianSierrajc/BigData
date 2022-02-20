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

header = {}

for l, line in enumerate(sys.stdin):
    words = line.strip('\n').split(',')
    if l == 0:
        for i, word in enumerate(words):
            header[word] = i
        continue 

    price, city, id = words[header[PRICE]], words[header[CITY]].strip(), words[header[ID]]
    city = re.sub("[^\w\s]", "", city)
    print("{}\t{}\t{}".format(city, price, id))
