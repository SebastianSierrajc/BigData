import sys

current_co = None
current_ci = None
count = 0

counties = {}

for line in sys.stdin:
    key, value = line.strip('\n').split('\t')
    if key == current_co:
        if value != current_ci:
            count += 1
            current_ci = value
    else:
        if current_co != None:
            if count in counties:
                counties[count] += 1
            else:
                counties[count] = 1
        current_co = key
        current_ci = value
        count = 1


for key, value in counties.items():
    print("{}\t{}".format(value, key))
