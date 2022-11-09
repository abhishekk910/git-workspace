class Node:
    def __init__(self, key):
        self.key = key 
        self.right = None 
        self.left = None 

# returns depth of leftmost leaf
def findDepth(node):
    d = 0
    while node != None:
        d += 1
        node = node.left
    return d 

# This function tests if a binary tree is perfect tree or not.
# All leaves are at same level
# All internal nodes have two children
def isPerfectTree(root, d, level = 0):
    # An empty tree is perfect
    if (root == None):
        return True
    
    # If leaf node, then its depth must
    # be same as depth of all other leaves.
    if (root.left == None and root.right == None):
        return (d == level + 1)

    # If internal node and one child is empty
    if (root.left == None or root.right == None):
        return False

    # Left and right subtrees must be perfect trees.
    return (isPerfectTree(root.left, d, level + 1) and isPerfectTree(root.right, d, level + 1))

# Wrapper over isPerfectRec()
def isPerfect(root):
    d = findDepth(root)
    return isPerfectTree(root, d)


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
# root.left.right.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

if (isPerfect(root)):
    print("It is Perfect Binary Tree")
else:
    print("It is Not a Perfect Binary Tree")



    