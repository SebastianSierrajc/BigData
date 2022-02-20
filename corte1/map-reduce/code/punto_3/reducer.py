import sys

current_k = None
current_v = float('inf')
current_id = None

for line in sys.stdin:
    key, value, id = line.strip('\n').split('\t')
    if current_k == key:
        if int(value) < current_v:
            current_v = int(value)
            current_id = id
    else:
        if current_k != None:
            print("{}\t{}\t{}".format(current_k, current_v, current_id))
        current_k = key
        current_v = int(value)
        current_id = id

print("{}\t{}\t{}".format(current_k, current_v, current_id))
