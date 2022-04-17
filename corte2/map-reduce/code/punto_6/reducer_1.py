import sys

key = None
current_key = None
current_count = 0
citys = {}

for row in sys.stdin:
    key, value = row.strip('\n').split('\t', 1)
    city, count = value.split(',', 1)
    count = int(count)

    if key == current_key:
        if city not in citys:
            citys[city] = True
            current_count += count
    else:
        if current_key:
            print("{}\t{}".format(current_key, current_count))
        current_key = key
        current_count = count
        citys = {city: True}

if key == current_key:
    print("{}\t{}".format(current_key, current_count))
