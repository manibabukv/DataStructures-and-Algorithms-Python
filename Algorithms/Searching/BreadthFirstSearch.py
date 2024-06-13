class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None
        self.num_of_nodes = 0

    def insert(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
            self.num_of_nodes += 1
            return
        else:
            current_node = self.root
            while (current_node.left != None) and (current_node.right != None):
                if newNode.data > current_node.data:
                    if current_node.right == None:
                        current_node.right == newNode
                        self.num_of_nodes += 1
                    else:
                        current_node = current_node.right
                elif newNode.data < current_node.data:
                    if current_node.left == None:
                        current_node.left = newNode
                        self.num_of_nodes += 1
                    else:
                        current_node = current_node.left
            return

    def lookup(self,data):
        if self.root == data:
            return "Found"

        current_node = self.root
        while True:
            if current_node.data == data:
                return "Found"
            if current_node == None:
                return "Not Found"
            elif data > current_node.data:
                current_node = current_node.right
            elif data < current_node.data:
                current_node = current_node.left


# from mycodeschool plus dsa course git repo
    def remove(self, data):
        if self.root == None:
            return None

        current_node = self.root
        parent_node = None

        while data != current_node.data:
            if data > current_node.data:
                parent_node = current_node
                current_node = current_node.right

            elif data < current_node.data:
                parent_node = current_node
                current_node = current_node.left

        # case 1: if current node is a leaf node
        if current_node.left == None and current_node.right == None:
            if parent_node == None:
                current_node == None
                return
            elif parent_node.data > current_node.data:
                parent_node.left = None
                return 
            elif parent_node.data < current_node.data:
                parent_node.right = None
                return

        # case 2: if current node have only one child
        if current_node.right == None:
            if parent_node == None:
                self.root = current_node.left
            elif parent_node.data > current_node.data:
                parent_node.left = current_node.left
                return 
            else:
                parent_node.right = current_node.left
                return

        if current_node.left == None:
            if parent_node == None:
                self.root == current_node.right
            elif parent_node.data > current_node.data:
                parent_node.left = current_node.right
                return
            else:
                parent_node.right = current_node.right
                return

        # case 3: if current node have two child nodes


        if current_node.right != None and current_node.left != None:
            del_node = current_node.right
            del_node_parent = current_node.right

            while del_node.left != None:
                del_node_parent = del_node
                del_node = del_node.left

            current_node.data = del_node.data

            if del_node_parent == del_node:
                current_node.right = del_node.right
                return
            elif del_node.right == None:
                del_node_parent.left == None
                return
            elif del_node.right != None:
                del_node_parent.left = del_node.right
                return
        return "Not Found"

        
    # BFS implementation on Binary Search Tree 
    # BFS implementation - Iterative Approach

    def BFS(self):
        current_node = self.root
        if current_node is None:
            return "Tree is Empty"
        BFS_result = []
        queue = [current_node]
        while len(queue) > 0:
            current_node = queue.pop(0)
            BFS_result.append(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return BFS_result
    
    # BFS implementation - Recursive Approach

    def BFSRecursive(self, queue, BFS_result):
        if self.root is None:
            return "Tree is Empty"

        if len(queue) == 0:
            return BFS_result
        
        current_node = queue.pop(0)
        BFS_result.append(current_node.data)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        return self.BFSRecursive(queue, BFS_result)


    
my_bst = BST()
my_bst.insert(5)
my_bst.insert(3)
my_bst.insert(7)
my_bst.insert(1)
my_bst.insert(13)
my_bst.insert(65)
my_bst.insert(0)
my_bst.insert(10)
'''
            5
        3       7
    1               13
0                10     65
'''

#The BFS Traversal for this tree should be : [5,3,7,1,13,0,10,65]

print(my_bst.BFS())
#[5, 3, 7, 1, 13, 0, 10, 65]

print(my_bst.BFSRecursive([my_bst.root],[])) #We need to pass the root node as an array and an empty array for the result
#[5, 3, 7, 1, 13, 0, 10, 65]


                
                


            

            
    





            