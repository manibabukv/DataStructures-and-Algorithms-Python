array = [2,1,4,1,5,2,6]


def first_rc(array):
    array_dict = {}
    for i in range(len(array)):
        if array[i] in array_dict:
            return array[i]
        else:
            array_dict[array[i]] = True
    return None

print(first_rc(array))




    
