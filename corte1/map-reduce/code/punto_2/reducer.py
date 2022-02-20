import sys

current_k = None
current_v = 0
current_c = 0

for line in sys.stdin:
    key, value = line.strip('\n').split('\t')
    if current_k == key:
        current_c += 1
        current_v += int(value)
    else:
        if current_k != None:
            print("{}\t{}".format(current_k, current_v / current_c))
        current_k = key
        current_v = int(value)
        current_c = 1

print("{}\t{}".format(current_k, current_v / current_c))
