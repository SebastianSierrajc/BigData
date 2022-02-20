from calendar import c
from site import venv
import sys

current_y = None
current_m = None
biggest_m = None
current_c = 0
biggest_c = 0

for line in sys.stdin:
    key, value = line.strip('\n').split('\t')

    if key == current_y:
        if value == current_m:
            current_c += 1
        else:
            if current_c > biggest_c:
                biggest_c = current_c
                biggest_m = current_m
            current_m = value
            current_c = 1
    else:
        if current_y != None:
            print("{}\t{}".format(current_y, biggest_m))
        current_y = key
        current_m = value
        biggest_m = None
        current_c = 1
        biggest_c = 0


print("{}\t{}".format(current_y, biggest_m))
