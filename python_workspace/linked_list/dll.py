"""
Doubly Linked List implementation in Python.
A doubly linked list is a linear data structure.
Elements are stored in the form of node.
Each node contains three sub-elements. prev, data, next
Data part stores the value of element.
Previos part stores the pointer to previous node.
next part stores the pointer to next node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None 
        self.next = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None 

    def print_list(self):
        temp = self.head
        if (temp != None):
            while (temp != None):
                print(f"{temp.data}->", end="")
                temp = temp.next
            print("None")
        else: 
            print("Linked List is Empty.")

    def prepend(self, data):
        newnode = Node(data)
        if(self.head) == None:
            self.head = newnode 
            return 
        else:
            self.head.prev = newnode
            newnode.next = self.head  
            self.head = newnode

    def append(self, data):
        newnode = Node(data)
        if (self.head) == None:
            self.head = newnode
            return 
        else:
            temp = self.head 
            while (temp.next) != None:
                temp = temp.next 
            temp.next = newnode
            newnode.prev = temp  

    def delete_at_front(self):
        if (self.head) != None:
            temp = self.head 
            self.head = self.head.next 
            temp = None 
            if (self.head != None):
                self.head.prev = None 

    def delete_at_last(self):
        if (self.head != None):
            if (self.head.next == None):
                self.head = None 
            else:
                temp = self.head
                while (temp.next.next != None):
                    temp = temp.next 
                lastnode = temp.next 
                temp.next = None 
                lastnode = None 

    def add_at(self, element, value):
        newnode = Node(element)
        if value < 1:
            print("position should be greater than or equal to 1.")
        elif (value == 1):
            newnode.next == self.head 
            self.head.prev = newnode
            self.head = newnode
        else:
            temp = self.head 
            for i in range(1, value-1):
                if (temp != None):
                    temp = temp.next 
            if (temp != None):
                newnode.next = temp.next 
                newnode.prev = temp 
                temp.next = newnode
                if (newnode.next != None):
                    newnode.next.prev = newnode
            else:
                print("Previous node is null")

    def count_nodes(self):
        temp = self.head 
        count = 0
        while (temp != None):
            count += 1
            temp = temp.next 
        print(f"Number of nodes : {count}") 

    def delete_all_nodes(self):
        while (self.head != None):
            # temp = self.head
            self.head = self.head.next
            # temp = None  
        print("All nodes deleted successfully..")

    def reverse_list(self):
        temp = None 
        cur = self.head 
        while (cur != None):
            temp = cur.prev 
            cur.prev = cur.next 
            cur.next = temp
            cur = cur.prev 
        if (temp != None):
            self.head = temp.prev 

        
dll = DoublyLinkedList()

dll.append(10)
dll.prepend(20)
dll.prepend(30)
dll.append(40)
dll.print_list()
dll.add_at(200, 2)
# dll.delete_at_front()
dll.print_list()
# dll.delete_at_last()
# dll.print_list()
dll.count_nodes()
dll.print_list()
# dll.delete_all_nodes()
dll.reverse_list()
dll.print_list()


