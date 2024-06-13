def DFS_inorder(self):
    return inorder_traversal(self.root, [])

def DFS_preorder(self):
    return preorder_traversal(self.root, [])

def DFS_postorder(self):
    return postorder_traversal(self.root, [])


def inorder_traversal(node, result):
    if node.left:
        return inorder(node.left, result)
    result.append(node.data)
    if node.right:
        return inorder(node.right, result)
    return result

def preorder_traversal(node, result):
    result.append(node.data)
    if node.left:
        return preorder_traversal(node.left, result)
    if node.right:
        return preorder_traversal(node.right, result)
    return result

def postorder_traversal(node, result):
    if node.left:
        return postorder_traversal(node.left, result)
    if node.right:
        return postorder_traversal(node.right, result)
    return result


# Iterative Approach

# Inorder

def inorder_iterative(self):
    curr_node = self.root
    stack = []
    result = []
    while curr_node or stack:
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left
        curr_node = stack.pop()
        result.append(curr_node.data)
        curr_node = curr_node.right
    return result

# Preorder

def preorder_iterative(self):
    curr_node = self.root
    result = [] 
    stack = []
    while curr_node or stack:
        while curr_node:
            result.append(curr_node.data)
            stack.append(curr_node.right)   # curr_node.right is something I was unable to figure out by myself
            curr_node = curr_node.left
        curr_node = stack.pop()
    return result 

     