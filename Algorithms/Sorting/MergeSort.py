# Implementation of Merge Sort

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def mergeSort(array):
    if len(array) == 1:
        return  array

    else:
        mid = len(array)//2
        left_array = array[:mid]
        right_array = array[mid:]
        print(f'Left : {left_array}')
        print(f'Right : {right_array}')
        return merge(mergeSort(left_array), mergeSort(right_array))


def merge(left, right):
    l = len(left)
    r = len(right)
    left_index = 0
    right_index = 0
    sorted_array = []
    while left_index < l and right_index < r:
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
    print(sorted_array + left[left_index:] + right[right_index:])
    return sorted_array + left[left_index:] + right[right_index:]


mergeSort(numbers)