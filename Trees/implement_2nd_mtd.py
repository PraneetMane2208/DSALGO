class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insert(root, newValue):
    # if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    # binary search tree is not empty, so we will insert it into the tree
    # if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild = insert(root.rightChild, newValue)
    return root
def findMin(root):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root


def sum(root):
    if root is None:
        return 0

    return root.data+sum(root.leftChild)+sum(root.rightChild)

    # sum(root.rightChild)


def deleteNode(root, val):
    if root is None:
        return
    if val < root.data:
        root.leftChild = deleteNode(root.leftChild, val)
    elif val > root.data:
        root.rightChild = deleteNode(root.rightChild, val)
    else:  # val == root.data
        if root.leftChild is None and root.rightChild is None:
            del root
            return None
        elif root.leftChild is not None and root.rightChild is None:
            temp = root.leftChild
            del root
            return temp
        elif root.leftChild is None and root.rightChild is not None:
            temp = root.rightChild
            del root
            return temp
        else:  # Node has two children
            temp = findMin(root.rightChild)
            root.data = temp.data
            root.rightChild = deleteNode(root.rightChild, temp.data)
            return root
    return root

def search(root, value):
    # Condition 1
    if root == None:
        return False
    # Condition 2
    elif root.data == value:
        return True
    # Condition 3
    elif root.data < value:
        return search(root.rightChild, value)
    # Condition 4
    else:
        return search(root.leftChild, value)


def inorder(root):
    if(root==None):
        return
    inorder(root.leftChild)
    print(root.data)
    inorder(root.rightChild)

def build_tree(elements):
    root = None
    for element in elements:
        root = insert(root, element)
    return root

from collections import deque

def level_order(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.data)

        if node.leftChild is not None:
            queue.append(node.leftChild)
        if node.rightChild is not None:
            queue.append(node.rightChild)

# def build_tree(elements):
#     insert(None,elements[0])
#     for i in range(1,len(elements)):
#         insert(root,elements[i])
#     return root



numbers=[17,4,1,20,9,23,18,34]
root=build_tree(numbers)
# inorder(root)
# deleteNode(root,9)
# inorder(root)
a=sum(root)
print(a)
level_order(root)
# root = insert(None, 15)
# insert(root, 10)
# insert(root, 25)
# insert(root, 6)
# insert(root, 14)
# insert(root, 20)
# insert(root, 60)
# print(search(root, 14))
# print(search(root, 22))