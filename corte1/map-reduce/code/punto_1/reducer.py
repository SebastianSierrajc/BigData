import sys

current_k = None
current_v = 0

for line in sys.stdin:
    key, value = line.strip('\n').split('\t')
    if current_k == key:
        current_v += int(value)
    else:
        if current_k != None:
            print(f"{current_k}\t{current_v}")
        current_k = key
        current_v = int(value)

print(f"{current_k}\t{current_v}")
