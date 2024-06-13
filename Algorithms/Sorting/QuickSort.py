# Implementation of Quick Sort

def swap(a,b,arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    start = pivot_index + 1
    end = len(elements) - 1

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        
        while elements[end] > pivot:
            end -= 1
        
        if start < end:
            swap(start, end, elements)
    
    swap(pivot_index, end, elements)

    return end

def quickSort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quickSort(elements, start, pi-1)
        quickSort(elements, pi+1, end)

if __name__ == '__main__':
    elements = [11, 9, 2, 7, 29, 15, 28]
    quickSort(elements, 0, len(elements)-1)
    print(elements)

