import sys
import re

for l, line in enumerate(sys.stdin):
    words = line.strip('\n').split(',')
    if l == 0: continue 
    date = words[2]
    year = date.split('-')[0]
    print(f"{year}\t{1}")
