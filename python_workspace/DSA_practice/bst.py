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
        if self.key == data:
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
<<<<<<< HEAD
        if self.key == data:
            print("Node is found in Binary Tree")
=======
        if data == self.key:
            print("Key is present in the tree")
>>>>>>> e9f316b99a290945f73b2db12264b8438ba70a84
            return 
        if data < self.key:
            if self.left:
                self.left.search(data)
            else:
<<<<<<< HEAD
                print("Node is not present in tree")
=======
                print("Key is not present in tree")
                return
>>>>>>> e9f316b99a290945f73b2db12264b8438ba70a84
        else:
            if self.right:
                self.right.search(data)
            else:
<<<<<<< HEAD
                print("Node is not present in tree")

    def delete(self, data, curr):
        if self.key is None:
            print("Binary Tree is Empty..")
            return 
        if data < self.key:
            if self.left:
                self.left = self.left.delete(data, curr)
            else:
                print("Given Node is not present in the tree")
        elif data > self.key:
            if self.right:
                self.right = self.right.delete(data, curr)
            else:
                print("Given Node is not present in the tree")
        else:
            if self.left is None:
                temp = self.right
                if data == curr:
                    self.key = temp.key
                    self.left = temp.left
                    self.right = temp.right 
                    temp = None 
                    return 
                self = None 
                return temp 
            if self.right is None:
                temp = self.left 
                if data == curr:
                    self.key = temp.key 
                    self.left = temp.left
                    self.right = temp.right 
                self = None 
                return temp 
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.delete(node.key, curr)
        return self 
=======
                print("Key is not present in tree")
                return

    def preorder(self):
        print(self.key, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
        
>>>>>>> e9f316b99a290945f73b2db12264b8438ba70a84

    def inorder(self):
        if self.left:
            self.left.inorder()
<<<<<<< HEAD
        print(self.key, end=' ')
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.key, end=' ')
        if self.left:
            self.left.inorder()
=======
        print(self.key, end=" ")
>>>>>>> e9f316b99a290945f73b2db12264b8438ba70a84
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
<<<<<<< HEAD
            self.left.inorder()
        if self.right:
            self.right.inorder()
        print(self.key, end=' ')

    def min_node(self):
        curr = self 
        while curr.left:
            curr = curr.left
        print("Minimum node in tree is ", curr.key) 

    def max_node(self):
        curr = self
        while curr.right:
            curr = curr.right
        print("Maximum node in tree is ", curr.key) 

def count(node):
    if node is None:
        return 0
    return 1 + count(node.left) + count(node.right)  

root = BST(10)
list1 = [20, 4, 30, 4, 1, 5, 6]
# list1 = [1,12]
list1 = [2, 1, 3, 9] 
for i in list1:
    root.insert(i)
print(count(root)) 
root.preorder()
print()
root.min_node()
root.max_node()
# if count(root) > 1:
#     root.delete(10, root.key)
# else:
#     print("Can't perform deletion operation") 
# root.preorder()
# root.preorder()
# print()
# root.delete(10)
# root.preorder()
# root.search(200)
=======
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
>>>>>>> e9f316b99a290945f73b2db12264b8438ba70a84
