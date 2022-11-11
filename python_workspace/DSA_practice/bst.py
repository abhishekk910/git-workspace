class BST:
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 

    def insert(self, data):
        if self.key == data:
            return 
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

    def search(self, data):
        if data == self.key:
            print("Key is present in the tree")
            return 
        if data < self.key:
            if self.left:
                self.left.search(data)
            else:
                print("Key is not present in tree")
                return
        else:
            if self.right:
                self.right.search(data)
            else:
                print("Key is not present in tree")
                return

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

root = BST(10)
# list1 = [100, 20, 5, 10, 150, 25, 120, 125, 200]
list1 = [6, 3, 1, 6, 7, 3, 98, 97, 101]
# list1 = [150, 70, 5, 25, 60, 100]
for i in list1:
    root.insert(i)
root.preorder()
print()
root.inorder()
print()
root.postorder()
print()
