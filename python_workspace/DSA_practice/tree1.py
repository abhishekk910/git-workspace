# Implementation tree traversal in python

class Node:
    def __init__(self, key):
        self.left = None 
        self.right = None 
        self.key = key 

    def preorder(self):
        print(self.key, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key, end=" ")
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key, end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Pre order Traversal:", end="")
root.preorder()
print()

print("In order Traversal:", end="")
root.inorder()
print()

print("Post order Traversal:", end="")
root.postorder()