"""
Doubly Linked List implementation in Python.
A doubly linked list is a linear data structure.
Elements are stored in the form of node.
Each node contains three sub-elements. prev, data, next
Data part stores the value of element.
Previos part stores the pointer to previous node.
next part stores the pointer to next node.
"""

from operator import ne


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

    def push_at(self, new_element, index):
        # create a new node 
        new_node = Node(new_element)
        if (index < 1):
            print("Index value should be greater than 1")
        elif (index == 1):
            new_node.next = self.head
            self.head = new_node 
        else:
            #make a temp node and traverse to the node previous to the index.
            temp = self.head 
            for i in range(1, index-1):
                if (temp != None):
                    temp = temp.next 
            # if previous node is not null, 
            if (temp != None):
                new_node.next = temp.next 
                new_node.prev = temp 
                temp.next = new_node 
                if (new_node.next != None):
                    new_node.next.prev = new_node 
                else:
                    print("The previous node is null.")

    def pop_at(self, index):
        if (index < 1):
            print("Index value should be greater than 1")
        elif(index == 1):
            self.head = self.head.next
        else:
            # make a temp node and traverse to node previous to index number.
            temp = self.head 
            for i in range(1, index-1):
                if (temp != None):
                    temp = temp.next 
            if (temp != None and temp.next != None):
                nodetodelete = temp.next 
                temp.next = temp.next.next 
                if (temp.next.next != None):
                    temp.next.next.prev = temp.next 
                nodetodelete = None 
            else:
                print("The node is already null.") 

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
        # If head is not null create three nodes.
        #  prevnode - pointing to head
        #  tempnode - pointing to head
        # currNode - pointing to next of head. 
        if (self.head != None):
            prev_node = self.head
            temp_node = self.head
            curr_node = self.head.next
            """
             #assign next and previous of the 
        #   prevNode as null to make the first 
        #   node as last node of the reversed list
            """
            prev_node.next = None 
            prev_node.prev = None 
            while (curr_node != None):
                """
                3. 
                While the curNode is not null adjust links 
         #   (unlink curNode and link it to the reversed list 
         #   from front and modify curNode and prevNode)
                """
                temp_node = curr_node.next 
                curr_node.next = prev_node 
                prev_node.prev = curr_node
                prev_node = curr_node
                curr_node = temp_node 

    def sort_list(self):
        if (self.head == None):
            print("Linked List is Empty.")
        else:
            curr = self.head
            while (curr.next != None):
                index = curr.next 
                while(index != None):
                    if(curr.data > index.data):    
                        index.data, curr.data = curr.data, index.data 
                    index = index.next
                curr = curr.next 
        
dll = DoublyLinkedList()
dll.append(10)
dll.prepend(20)
dll.prepend(30)
dll.append(40)
dll.print_list()
# dll.add_at(200, 2)
# # dll.delete_at_front()
# dll.print_list()
# # dll.delete_at_last()
# # dll.print_list()
# dll.count_nodes()
# dll.print_list()
# # dll.delete_all_nodes()
# dll.reverse_list()
# dll.print_list()
dll.push_at(100, 2)
dll.print_list()
dll.pop_at(2)
dll.print_list()
dll.sort_list()
dll.print_list()
dll.reverse_list()
dll.print_list()



