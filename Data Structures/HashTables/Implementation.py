class HashTable():
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size
    
    def __str__(self):
        return (self.__dict__)

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]+i))*self.size
        return hash

    
myHashTable = HashTable(50)

print(_hash('grapes')) 