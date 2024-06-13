# Implementation of Insertion Sort

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertionSort(array):
    for i in range(1, len(array)):
            current = array[i]
            j = i-1
            while j >= 0 and array[j] > current:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = current  
    return array


print(insertionSort(numbers))

j = 0

[99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

j = 1




