import sys

curr_key = None
curr_value = 0
curr_count = 0

for row in sys.stdin:
    key, value, count = row.strip('\n ').split('\t')
    value = int(value)
    count = int(count)

    if key == curr_key:
        if count > curr_count:
            curr_value = value
            curr_count = count
    else:
        if curr_key:
            print('{}\t{}\t{}'.format(curr_key, curr_value, curr_count))
        curr_key = key
        curr_value = value
        curr_count = count

if curr_key == key:
    print('{}\t{}\t{}'.format(curr_key, curr_value, curr_count))
