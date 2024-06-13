class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length = 1
        else: 
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    def prepend(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.length = 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.length += 1

    def print_list(self):
        if self.head is None:
            print("Empty")
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data, end = ' ')
                current_node = current_node.next
        print()
    
    def insert(self, position, data):
        newNode = Node(data)
        if position >= self.length:
            if position > self.length:
                print("This position is not available. Inserting at the end of the list.")
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
        elif position == 0:
            newNode.next = self.head
            self.head = newNode
            self.length += 1
        else:
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next
            newNode.next = current_node.next
            current_node.next = newNode
            self.length += 1



    def del_by_value(self, data):
        if self.head == None:
            print("LinkedList is empty. Nothing to print")
            return
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        
        while current_node.next != None and current_node.data != data:
            current_node = current_node.next

        print(current_node)
        if current_node.next == None:
            self.tail = current_node
            self.length -= 1
        elif current_node.next != None:
            current_node.next = current_node.next.next
            if current_node.next == None:
                self.tail = current_node
                self.length -= 1
        else:
            print("Give element is not found")

        
    def del_by_position(self, position):
        if self.head == None:
            print("LinkedList is empty. Nothing to delete")
            return
        
        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        current_node = self.head
        for i in range(position-1):
            current_node = current_node.next
        current_node.next = current_node.next.next

        if current_node.next == None:
            self.tail = current_node
            return
        self.length -= 1

if __name__ == '__main__':
    my_linked_list = LinkedList()
    my_linked_list.print_list()

    my_linked_list.append(5)
    my_linked_list.append(2)
    my_linked_list.append(9)
    my_linked_list.print_list()

    my_linked_list.prepend(4)
    my_linked_list.print_list()

    my_linked_list.insert(2,7)
    print(my_linked_list.length)
    my_linked_list.print_list()

    my_linked_list.del_by_value(3)
    my_linked_list.print_list()

    my_linked_list.insert(0,0)
    my_linked_list.insert(6,0)
    my_linked_list.insert(9,3)
    my_linked_list.print_list()

    my_linked_list.del_by_value(3)
    my_linked_list.print_list()