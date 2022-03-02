import sys
import array
import time
from multiprocessing import shared_memory
from collections import Counter


print('Client3 is ready')

shm = shared_memory.SharedMemory(name=sys.argv[-1].strip())
while shm.buf[0] == 0:
    time.sleep(1)
count_mapping = Counter(list(array.array('b', shm.buf[1:shm.buf[0] + 1])))
mode = []
most_common = None
for value, count in count_mapping.most_common():
    if most_common is not None and most_common != count:
        break
    most_common = count
    mode.append(str(value))

print(f"Mode is	{','.join(mode)}")
shm.close()