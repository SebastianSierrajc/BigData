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
    price, city = words[1], words[6].strip()
    city = re.sub("[^\w\s]", "", city)
    print("{}\t{}".format(city, price))
