from email import header
from os import curdir
from turtle import position


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class Circular_Linked_List:
    def __init__(self):
        self.head = None 

    # traversal of linked list. 
    def print_list(self):
        temp = self.head
        if temp != None:
            while True:
                print(f"{temp.data}", end="->")
                temp = temp.next 
                if (temp == self.head):
                    break 
            print("nil")
        else:
            print("Linked List contains no elements..") 

    # adding element at the starting of the linked list.
    def prepend(self, element):
        new_node = Node(element) 
        if self.head == None:
            self.head = new_node 
            new_node.next = self.head 
            return 
        else:
            temp = self.head 
            while (temp.next != self.head):
                temp = temp.next 
            temp.next = new_node
            new_node.next = self.head  #shifting current 1st node to 2nd node
            self.head = new_node   #pointing head to new node .

    # adding elments at the end of the linked list.
    def append(self, element):
        new_node = Node(element)
        if self.head == None:
            self.head = new_node 
            new_node.next = self.head 
            return 
        else:
            temp = self.head 
            while (temp.next != self.head):
                temp = temp.next 
            temp.next = new_node #current last node pointing to new node.
            new_node.next = self.head #new last node pointing to self.head 

    # deleting elements at the starting of the linked list. 
    def delete_at_start(self):
        if self.head == None:
            print("Linked List is empty..")
            return 
        else:
            if (self.head.next == self.head):
	            self.head = None
            else:
                temp = self.head 
                while (temp.next != self.head):
                    temp = temp.next 
                self.head = self.head.next ##Make head as next of head(pointing to current 2nd Node)
                temp.next = self.head #Make next of last node as head

    # deleting elements at the ending of the linked list. 
    def delete_at_end(self):
        if self.head == None:
            print("Linked List is empty..")
            return 
        else:
            if (self.head.next == self.head):
                self.head = None 
            else:
                temp = self.head 
                while (temp.next.next != self.head):
                    temp = temp.next 
                temp.next = self.head #making last 2nd node to point towards to head node , deleting last node. 

    # counting number of nodes in linked list.
    def count_nodes(self):
        temp = self.head 
        i = 0 
        if (temp != None):
            while True:
                temp = temp.next 
                i += 1
                if (temp == self.head):
                    break
        print(f"Number of nodes in linked list : ", i) 

    # deleting nodes in linked list.
    def delete_all_nodes(self):
        if self.head == None:
            print("Linked List is Empty..")
        else:
            if (self.head.next == self.head): #if there is only one node, point head to None 
                self.head = None 
            else:
                current = self.head 
                while (current != self.head):
                    temp = current.next # store current next in temp. 
                    current = None #delete current node. 
                    current = temp #move current to next using temp, repeating the process till current reaches the head.
                self.head = None #delete the head. 

# This function sorts the list in ascending order
    def sortList(self):
        if self.head == None:
            print("Linked List is Empty.")
        # Current will point to head 
        else:
            curr = self.head 
            while True:
                index = curr.next 
                while (index != self.head):
                    # If current node is greater than index data, swaps the data    
                    if (curr.data > index.data):
                        curr.data, index.data = index.data, curr.data 
                    index = index.next 
                curr = curr.next 
                if (curr.next == self.head):
                    break 

    def reverseList(self):
  #1. If head is not null create three nodes
  #   prevNode - pointing to head,
  #   tempNode - pointing to head,
  #   curNode - pointing to next of head
        if(self.head != None):
            prevNode = self.head
            tempNode = self.head
            curNode = self.head.next
            
            #2. assign next of prevNode as itself to make the
            #   first node as last node of the reversed list
            prevNode.next = prevNode
            
            while(curNode != self.head):
            #3. While the curNode is not head adjust links 
            #   (unlink curNode and link it to the reversed list 
            #   from front and modify curNode and prevNode) 
                tempNode = curNode.next
                curNode.next = prevNode
                self.head.next = curNode
                prevNode = curNode
                curNode = tempNode

            #4. Make prevNode (last node) as head
            self.head = prevNode 

    def push_at(self, element, index):
        """
        allocate node to new element and create a temp node to traverse the list
        """
        new_node = Node(element)
        temp = self.head 
        no_of_elements = 0 

        # find number of elements.
        if (temp != None):
            no_of_elements += 1 
            temp = temp.next 
        while (temp != self.head):
            no_of_elements += 1
            temp = temp.next 
        
        # check if adding index is valid.
        if (index < 1 or index > (no_of_elements+1)):
            print("Invalid Index.")
        elif index == 1:
            # if index is 1, make next of new node as head and new node as head 
            if (self.head == None):
                self.head = new_node 
                self.head.next = self.head 
            else:
                while (temp.next != self.head):
                    temp = temp.next 
                new_node.next = self.head 
                self.head = new_node 
                temp.next = self.head 
        else:
            temp = self.head 
            for i in range(1, index-1):
                temp = temp.next
            new_node.next = temp.next 
            temp.next = new_node 

    # delete a node at the given index.
    def pop_at(self, index):
        # create two nodes temp and nodeToDelete to traverse and track the node to delete 
        nodeToDelete = self.head 
        temp = self.head 
        no_of_elements = 0 

        # find the number of elements in the list 
        if (temp != None):
            no_of_elements += 1 
            temp = temp.next 
        while (temp != self.head):
            no_of_elements += 1
            temp = temp.next 

        # check if the specified position is valid 
        if ((index < 1) or (index > no_of_elements)):
            print("Invalid Position")
        elif (index == 1):
            #  if the index is 1 and head is the only element in the list,  make it null,else make next of head as new head and adjust links accordingly.
            if (self.head.next == self.head):
                self.head = None 
            else:
                while (temp.next != self.head):
                    temp = temp.next 
                self.head = self.head.next 
                temp.next = self.head 
                nodeToDelete = None 
        else:
            # Else, traverse to node previous to the given index and delete the given node and adjust links accordingly.
            temp = self.head 
            for i in range(1, index-1):
                temp = temp.next
            nodeToDelete = temp.next 
            temp.next = temp.next.next 
            nodeToDelete = None 


list1 = Circular_Linked_List()

list1.append(10)
list1.append(20)
list1.prepend(30)
list1.prepend(100)
list1.print_list()
list1.push_at(200, 2) 
list1.print_list()
list1.pop_at(5)
list1.print_list()
