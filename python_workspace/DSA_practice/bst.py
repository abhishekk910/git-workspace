class BST:
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 

    def insert(self, data):
        if self.key is None:
            self.key = data 
            return 
        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

root = BST(10)
list1 = [20, 4, 30, 4, 1, 5, 6]
for i in list1:
    root.insert(i)

# root = BST(10)
# print(root.key, root.left, root.right)
# root.left = BST(5)
# root.right = BST(15)
# print(root.key, root.left, root.right)
# print(root.left.key, root.left.left, root.left.right)
# print(root.right.key, root.right.left, root.right.right)
