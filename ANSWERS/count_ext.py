import sys
import os
from collections import Counter

start_dir = sys.argv[1]

counter = Counter()

for curr_dir, dir_list, file_list in os.walk(start_dir):
    for file_name in file_list:
        if '.' in file_name:
            # parts = file_name.split('.')
            # ext = parts[-1]
            base, ext = os.path.splitext(file_name)
            counter[ext] += 1

for ext, count in counter.items():
    print(ext, count)
print()

print(counter.most_common(10))
