# You are given two arrays you need to find whether these two arrays have anything in common or not

array1 = ['a','b', 'c', 'd', 'x']
array2 = ['x','y','z']

# Brute force solution

def brute_force_common_element(array1, array2):
    for i in array1:
        for j in array2:
            if i == j:
                return "Yes"
    return "No"

print(brute_force_common_element(array1, array2))

# The time complexity of the above approach is O(m*n) since m and n are two arrays, which is horrible let's try to optimize it

array1 = ['a','b', 'c', 'd', 'x']
array2 = ['x','y','z']

def better_common(array1, array2):
    try:
        array1_dict = dict()
        for i in array1:
            if i not in array1_dict:
                array1_dict[i] = True
        
        for i in array2:
            if i in array1_dict:
                return "Yes"      
        return "No"
    
    except TypeError:
        return "Exactly two arrays are required"

print(better_common(array1, array2))

# The time complexity of the above approach is O(m+n) much better than O(m*n)