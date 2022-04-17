import sys

header = sys.stdin.readline()

for row in sys.stdin:
    cols = row.strip('\n ').split(',')
    date = cols[2].split('-')
    year = int(date[0])
    month = int(date[1])
    print("{}-{}\t{}".format(year, month, 1))
