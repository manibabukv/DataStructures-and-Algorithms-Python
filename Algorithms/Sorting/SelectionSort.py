# Selection Sort Implementation

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(array):
    for i in range(len(array)-1):
        minimum = array[i]
        minimum_index = i
        for j in range(i+1, len(array)):
            if array[j] < minimum:
                minimum = array[j]
                minimum_index = j
        if minimum_index != i:
            array[minimum_index], array[i] = array[i], array[minimum_index]
    return array

print(selectionSort(numbers))
