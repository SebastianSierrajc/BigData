import sys

current_key = None
key = None
current_count = 0

for row in sys.stdin:
    key, count = row.strip('\n').split('\t', 1)
    count = int(count)

    if key == current_key:
        current_count += count
    else:
        if current_key:
            print("{}\t{}".format(current_key, current_count))
        current_key = key
        current_count = count

if key == current_key:
    print("{}\t{}".format(current_key, current_count))
