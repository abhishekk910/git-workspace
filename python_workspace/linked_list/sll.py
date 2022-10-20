# node structure 
from locale import currency
from os import link
from turtle import position


class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None 

# class Linked List 
class Linked_List():
    def __init__(self):
        self.head = None 

    #Adding element at the start of the linked list
    def prepend(self, element):
        newNode = Node(element)
        newNode.next = self.head
        self.head = newNode 

    #Adding element at the end of the linked list
    def append(self, element):
        newnode = Node(element)
        if (self.head == None):
            self.head = newnode
            return
        temp = self.head 
        while (temp.next != None):
            temp = temp.next 
        temp.next = newnode 

    # removing elements at the end of the linked list
    def remove_at_first(self):
        if self.head == None:
            print("Linked List is empty.")
            return
        self.head = self.head.next 

    def remove_at_last(self):
        if (self.head == None):
            print("Linked List is Empty..")
            return 
        temp = self.head
        while (temp.next.next != None):
            temp = temp.next 
        lastnode = temp.next
        temp.next = None 
        lastnode = None 

    # traversal
    def print_list(self):
        if self.head == None:
            print("Linked List is empty.")
            return
        temp = self.head
        while (temp != None):
            print(f"{temp.data} ->", end=" ")
            temp = temp.next 
        print("Null")

    def reverse_list(self):
        if (self.head != None):
            prevNode = self.head #prevnode pointing to head
            tempNode = self.head #pointing to head 
            currNode = self.head.next #pointing to next of head
            # assign next of prevNode as null to make the
            # first node as last node of the reversed list
            prevNode.next = None 

            while (currNode != None):
                #  While the curNode is not null adjust links 
                # (unlink curNode and link it to the reversed list 
                #from front and modify curNode and prevNode)
                tempNode = currNode.next
                currNode.next = prevNode
                prevNode = currNode
                currNode = tempNode

            # Make prevNode (last node) as head
            self.head = prevNode 

    def sort_list(self):
        curr = self.head 
        index = None 
        if (self.head == None):
            print("Linked List is empty..")
            return
        else:
            while (curr != None):
                #Node index will point to node next to current  
                index = curr.next
                while (index != None):
                    if (curr.data > index.data):
                        temp = curr.data
                        curr.data = next.data
                        index.data = temp 
                    index = index.next 
                curr = curr.next 

    def searchElement(self, search_elemnt):
        # create a temp node pointing to node 
        temp = self.head 
        flag = False
        i = 0
        """
        if the temp node is not null check the
        node value with searchValue, if found 
        update variables and break the loop, else
        continue searching till temp node is not null 
        """
        if (temp != None):
            while (temp != None):
                i += 1
                if (temp.data == search_elemnt):
                    flag = True 
                    break 
                temp = temp.next 
            if (flag == True):
                print(f"{search_elemnt} is found at index =", i)
            else:
                print(f"{search_elemnt} is not found.")
            
        else:
            """
            If the temp node is null at the start, the list is empty.
            """
            print("The list is empty.")

    # adding value at the index value. 
    def push_at(self, new_element, index):
        new_node = Node(new_element)
        if (index < 1):
            print("index should be greater than 0")
        elif (index == 1):
            new_node.next = self.head
            self.head = new_node 
        else:
            temp = self.head
            for i in range(1, index-1):
                if (temp != None):
                    temp = temp.next 
            """
            If the previous node is not null, make 
            newNode next as temp next and temp next 
            as newNode.
            """
            if (temp != None):
                new_node.next = temp.next 
                temp.next = new_node 
            else:
                print("Previous node is null..")

    #deleting value at index value.
    def pop_at(self, index):
        if (index < 1):
            print("Index value should be greater than zero")
        elif (index == 1):
            self.head = self.head.next 
        else:
            """
            Make  a temp node and traverse to the temp previous to the position. 
            """
            temp = self.head 
            for i in range(1, index-1):
                if (temp != None):
                    temp = temp.next 

            if (temp != None and temp.next != None):
                nodetodelete = temp.next 
                temp.next = temp.next.next
                nodetodelete = None 
            else:
                print("The node is null.") 


linked_list = Linked_List()
linked_list.print_list() 
# linked_list.prepend(20)
# linked_list.append(10)
# linked_list.prepend(30)
# linked_list.prepend(40)
# linked_list.print_list()
# linked_list.searchElement(30) 
# linked_list.reverse_list()
# linked_list.print_list()
# linked_list.pop_at(1) 
# linked_list.remove_at_first()
# linked_list.remove_at_last()
# linked_list.print_list()
# linked_list.push_at(200, 2)
# linked_list.print_list()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.print_list() 
linked_list.pop_at(2)
linked_list.print_list() 
linked_list.push_at(100, 3) 
linked_list.print_list()
