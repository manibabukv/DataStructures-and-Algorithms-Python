import time, random


times = []

def squared_without_memoization(n):
    return n**2

array = [random.randint(1,10) for _ in range(1000000)]

t1 = time.time()

for i in range(len(array)):
    print(squared_without_memoization(array[i]))

t2 = time,time()

times.append(t2-t1)

# Memoization implementation

cache = {}

def squared_with_memoization(n):
    if n in cache:
        return cache[n]
    else:
        cache[n] = n**2
    return cache[n]

t1 = time.time()
for i in range(len(array)):
    print(squared_with_memoization(array[i]))
t2 = time.time()
times.append(t2-t1)

from functools import lru_cache

@lru_cache(maxsize=10000)
def squaring(number):
    return  number**2

print(array)
t1 = time.time()
for i in range(len(array)):
    print(squaring(array[i]))
t2 = time.time()
times.append(t2-t1)

print(times)
