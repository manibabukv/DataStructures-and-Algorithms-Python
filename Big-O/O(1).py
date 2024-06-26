# O(n) - Constant Time
# The no. of operation do not depend on the size of the input and are always constant.

import time

array_small = ['nemo' for i in range(10)]
array_medium = ['nemo' for i in range(100)]
array_large = ['nemo' for i in range(100000)]

def finding_nemo(array):
    t0 = time.time()
    print(array[0]) #O(1) Operation
    print(array[1]) #0(1) Operation
    t1 = time.time()
    print(f'Time Taken = {t1-t0}')

finding_nemo(array_small)
finding_nemo(array_medium)
finding_nemo(array_large)

# The time taken in all the above cases will be 0.0 since we are only taking the first and second element.
# We are not looping over the entire array
# We are performing two O(1) operations, which equal to O(2)
# Any constant number can be considered as 1. There we can say O(1) Constant Time Complexity

boxes = ['a','b','c','d','e']

for i in boxes:
    for j in boxes:
        print(f'({i},{j})')