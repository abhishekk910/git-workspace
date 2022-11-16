# Implementation of stack using Linked List

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class Stack:
    def __init__(self):
        self.head = None 
        self.top = None 
        self.nodesCount = 0

    def traversal(self):
        temp = self.head #temporary pointer to point to head
        while temp != None: #iterating over stack
            print(temp.data, end=" ")
            temp = temp.next 
        print()

    def is_Empty(self):
        if self.head == None:
            return True 
        return False 

    def push(self, e):
        if self.head == None and self.top == None:
            self.head = e 
            self.top = e 
        else:
            self.top.next = e 
            self.top = e 
        self.nodesCount += 1

    def pop(self):
        if self.head == None and self.top == None:
            print("Stack is Empty")
            return 
        else:
            ele = self.top.data 
            if self.top == self.head: #only one node 
                self.top = None
                self.head = None 
            else:
                temp = self.head 
                while temp.next != self.top:
                    temp = temp.next 
                temp.next = None 
                self.top = temp 
        self.nodesCount -= 1
        return ele 

    def size(self):
        return self.nodesCount 

    def peek(self):
        if self.head == self.top:
            print("Stack is Empty.")
            return 
        else:
            e = self.top.data
            return e 


s = Stack()
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

print(s.is_Empty())
s.push(node1)
s.push(node2)
s.push(node3)
s.traversal()
print(s.peek()) 
# print(s.pop())
print(s.size())
s.traversal()
print(s.is_Empty())
print(s.peek())