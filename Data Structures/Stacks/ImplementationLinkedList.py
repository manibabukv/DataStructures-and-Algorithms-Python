class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top is None:
            return None
        return self.top

    def push(self, data):
        newNode = Node(data)
        if self.top is None:
            self.top = newNode
            self.bottom = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.length += 1

    
    def pop(self):
        if self.top is None:
            print("The Stack is Empty")
        else:
            self.top = self.top.next
            self.length -= 1
            if self.length == 0:
                self.bottom = None
    
    def print_stack(self):
        if self.top is None:
            print("The Stack is Empty")
        else:
            current_pointer = self.top
            while current_pointer:
                print(current_pointer.data)
                current_pointer = current_pointer.next


my_stack = Stack()
print(my_stack.peek())
#None

my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
my_stack.print_stack()
#discord
#udemy
#google

print(my_stack.top.data)
#discord

print(my_stack.bottom.data)
#gogle

my_stack.pop()
my_stack.print_stack()
#udemy
#google

my_stack.pop()
my_stack.pop()
my_stack.print_stack()
#Stack Empty


