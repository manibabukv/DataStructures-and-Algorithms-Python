class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.data

    def enqueue(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.last = newNode
            self.first = self.last
            self.length += 1
            return
        else:
            self.last.next = newNode
            self.last = newNode
            self.length += 1
            return

    def dequeue(self):
        if self.length == 0:
            print("Queue is Empty")
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return

    def print_queue(self):
        if self.length == 0:
            print("Queue Empty")
            return
        else:
            current_pointer = self.first
            while(current_pointer!= None):
                if current_pointer.next == None:
                    print(current_pointer.data)
                else:
                    print(f'{current_pointer.data}  <<--  ', end='')
                current_pointer = current_pointer.next
            return

my_queue = Queue()
my_queue.enqueue("This")
my_queue.enqueue("is")
my_queue.enqueue("a")
my_queue.enqueue("Queue")
my_queue.print_queue()
#This  <<--  is  <<--  a  <<--  Queue

print(my_queue.peek())
#This

my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()
#a  <<--  Queue

print(my_queue.__dict__)
#{'first': <__main__.Node object at 0x0000020CE99AED48>, 'last': <__main__.Node object at 0x0000020CE99AED88>, 'length': 2}
print(my_queue.first)
#<__main__.Node object at 0x000001A3F633ED48>
print(my_queue.first.data)
#a

my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()
#Queue Empty