import sys


CITY = 'STAMFORD'
prices = []

for line in sys.stdin:
    key, value = line.strip('\n').split('\t')
    if key == CITY:
        prices.append((key, int(value)))

for key, value in sorted(prices, key=lambda x: x[1]):
    print("{}\t{}".format(key, value))
