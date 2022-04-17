import sys

curr_key = None
curr_value = 0

for row in sys.stdin:
    key, value = row.strip('\n ').split('\t')
    value = int(value)

    if key == curr_key:
        curr_value += value
    else:
        if curr_key:
            print('{}\t{}'.format(curr_key, curr_value))
        curr_key = key
        curr_value = value

if curr_key == key:
    print('{}\t{}'.format(curr_key, curr_value))
