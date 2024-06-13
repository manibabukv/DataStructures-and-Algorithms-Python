# Arrays are most common used data structure, In Python arrays are basically lists
# Arrays are of two types: Static and Dynamic Arrays
# In Python we only have Dynamic Arrays

"""Basic Arrays/Lists Methods
     1. Look-up/Access -- Big O(1)
     2. Push/pop -- Big O(1)
     3. Insert -- Big O(n)
     4. Delete -- Big O(n)"""



# Now let's have a look at these methods

# Access or Look-up
array = [5,8,2,9,17,43,25,10]

print(array[1])
print(array[5])

# Push/pop
array = [5,8,2,9,17,43,25,10]

array.pop()
print(array)

# Insert 
array = [5,8,2,9,17,43,25,10]

array.insert(0, 50)
print(array)

# Delete 
array = [5,8,2,9,17,43,25,10]

array.remove(17)
array.pop(0)
del array[2:4]
print(array)