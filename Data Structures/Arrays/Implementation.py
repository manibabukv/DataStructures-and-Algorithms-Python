# Although all the array/list are in-built in the Python, let's try to build the array and its method from scratch

class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}
        
    def __str__(self):
        return (self.__dict__)

    def get(self, index):
        return self.data[index]

    def get(self, item):
        self.length += 1
        self.data[self.length-1] = item

    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item

    def insert(self, index, item):
        self.length += 1
        for i in range(index, self.length):
            self.data[i+1] = self.data[i]
        self.data[index] = item
        return self.data
    
    def delete(self, index):
        for i in range(index, self.length):
            self.data[i+1] = self.data[i]
        del self.data[self.length-1]
        self.length()




arr = MyArray()
arr.push(6)
print(arr)
#{'length': 1, 'data': {0: 6}}

arr.push(2)
print(arr)
#{'length': 2, 'data': {0: 6, 1: 2}}

arr.push(9)
print(arr)
#{'length': 3, 'data': {0: 6, 1: 2, 2: 9}}

arr.pop()
print(arr)
#{'length': 2, 'data': {0: 6, 1: 2}}

arr.push(45)
arr.push(12)
arr.push(67)
print(arr)
#{'length': 5, 'data': {0: 6, 1: 2, 2: 45, 3: 12, 4: 67}}

arr.insert(3,10)
print(arr)
#{'length': 6, 'data': {0: 6, 1: 2, 2: 45, 3: 10, 4: 12, 5: 67}}

arr.delete(4)
print(arr)
#{'length': 5, 'data': {0: 6, 1: 2, 2: 45, 3: 10, 4: 67}}

print(arr.get(1))
print(arr) 