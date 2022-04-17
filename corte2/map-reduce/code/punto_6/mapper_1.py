import sys

header = sys.stdin.readline()

for row in sys.stdin:
    cols = row.strip('\n ').split(',')
    city = cols[6].upper()
    county = cols[8].upper()
    print("{}\t{},{}".format(county, city, 1))
