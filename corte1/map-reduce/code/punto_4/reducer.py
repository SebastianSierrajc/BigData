import sys


CITY = 'STAMFORD'
DATE = '2015'
prices = []

for line in sys.stdin:
    key, date, value = line.strip('\n').split('\t')
    if key == CITY and date == DATE:
        prices.append((key, int(value)))

for key, value in sorted(prices, key=lambda x: x[1]):
    print("{}\t{}".format(key, value))
