array = [1,2,4,5]
sum = 3

# Brute Force Solution
def brute_force_pair_sum(array, sum):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] + array[j+1] == sum:
                return True
                break
        return False

print(brute_force_pair_sum(array, sum))

# The Time Complexity of this approach is n^2 which is horrible for large inputs

array = [1,2,4,5]
sum = 3

def binary_search(array, left, right, ele):
    if right >= left:
        mid = left+right//2
        if (array[mid]) == ele:
            return True
        elif array[mid] > ele:
            return binary_search(array, left, mid-1, ele)
        else: 
            return binary_search(array, mid+1, right, ele)
    else:
        return False

def slightly_better_pair_sum(array, sum):
    left = 0
    right = len(array) - 1
    for i in array:
        comp = sum - i
        if binary_search(array, left, right, comp):
            return "Yes"
    return "No"

print(slightly_better_pair_sum(array, sum))

# The Time Complexity of this one is O(nlogn) better than O(n^2)

array = [1,2,4,5]
sum = 3


def smart_pair_sum(array, sum):
    left = 0
    right = len(array) - 1
    while right  > left:
        if array[left] + array[right] == sum:
            return "Yes"
        elif array[left] + array[right] > sum:
            right -= 1
        else:
            left += 1
    return "No"

print(smart_pair_sum(array, sum))

# The Time Complexity of this one is O(n)

# What if the array is not sorted? We can use the sort funtion

array = [1,2,4,5]
sum = 3

def sort_pair_sum(array, sum):
    array.sort()
    left = 0
    right = len(array) - 1
    while right  > left:
        if array[left] + array[right] == sum:
            return "Yes"
        elif array[left] + array[right] > sum:
            right -= 1
        else:
            left += 1
    return "No"

print(sort_pair_sum(array, sum))


# There is a better way of doing this

array = [1,2,4,5]
sum = 3

def pair_sum(array, sum):
    comp_dict = dict()
    for value in array:
        comp = sum - value
        if comp in comp_dict:
            return "Yes"
        else:
            comp_dict[value] = True
    return "No"

print(pair_sum(array, sum))

# This one has a better time complexity of O(n)