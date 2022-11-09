# full binary tree 

# creating a node
class Node:

    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 

# Checking full binary tree
def isFullTree(root):

    # if empty tree
    if root is None:
        return True 
    
    # leaf node 
    if root.left is None and root.right is None:
        return True 

    """
    If both left and right subtress are not None and left and right subtress are full
    """
    if root.left is not None and root.right is not None:
        return (isFullTree(root.left) and isFullTree(root.right))

    # if none of the above conditions doesn't apply 
    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
# root.left.left.left = Node(40)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

if isFullTree(root):
    print ("The Binary tree is full")
else:
    print ("Binary tree is not full")