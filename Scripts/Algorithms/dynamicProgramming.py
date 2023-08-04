import time
import random
from functools import lru_cache

array = [random.randint(0, 9) for _ in range(100000)]

def square_itrative(num):
    return num ** 2
times = []

t1 = time.time()
for i in range(len(array)):
    print(square_itrative(array[i]))
t2 = time.time()

times.append(t2 - t1)


cache = {}
def square_memoization(num):
    if num in cache:
        return cache[num]
    else:
        cache[num] = num ** 2
        return cache[num]

t1 = time.time()
for i in range(len(array)):
    print(square_memoization(array[i]))
t2 = time.time()

times.append(t2 - t1)


@lru_cache(maxsize=1000)
def squaring(num):
    return num ** 2

t1 = time.time()
for i in range(len(array)):
    print(squaring(array[i]))
t2 = time.time()

times.append(t2 - t1)

print(times)
