import sys

for row in sys.stdin:
    key, value = row.strip('\n ').split('\t', 1)
    print("{}\t{}".format(value, 1))
