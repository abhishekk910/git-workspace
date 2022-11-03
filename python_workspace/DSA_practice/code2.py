# Implementation of queue using Linked Lists

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None 


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None 
        self.nodesCount = 0

    def traversal(self):
        temp = self.head #temporary pointer to point to head
        while temp != None: #iterating over stack
            print(temp.data, end=" ")
            temp = temp.next 
        print()

    def enqueue(self, new_element):
        if self.head == None and self.tail == None:
            self.head = new_element
            self.tail = new_element
        else:
            self.tail.next = new_element
            self.tail = new_element 
        self.nodesCount += 1

    def dequeue(self):
        if self.head == None and self.tail == None:
            print("Queue is Empty")
            return 
        else:
            self.head = self.head.next 
        self.nodesCount -= 1 

    def peek(self):
        if self.head == None:
            return False
        return self.head.data 

    def is_empty(self):
        if self.head == None and self.tail == None:
            return True
        return False
    
    def get_size(self):
        return self.nodesCount

q = Queue()
print(q.is_empty())
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
q.enqueue(node1)
q.enqueue(node2)
q.enqueue(node3)
q.traversal()
print(q.get_size())
q.dequeue()
print(q.get_size())
q.traversal()
print(q.peek())
