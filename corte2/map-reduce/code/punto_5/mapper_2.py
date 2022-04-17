import sys

for row in sys.stdin:
    cols = row.strip('\n ').split('\t')
    date = cols[0].split('-')
    year = int(date[0])
    month = int(date[1])
    count = int(cols[1])
    print("{}\t{}\t{}".format(year, month, count))
