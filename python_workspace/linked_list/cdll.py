# Implemenetation of Circular Doubly Linked List in Python.

class Node:
    # constructor to create a new node.
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.prev = None 

class LinkedList:
    # constructor to create an empty LinkedList
    def __init__(self):
        self.head = None 

    # traversal of elements. 
    def print_list(self):
        temp = self.head 
        if (temp != None):
            while True:
                print(temp.data, end=" ")
                temp = temp.next 
                if (temp == self.head):
                    break 
            print()
        else:
            print("The Linked list is empty..")

    # adding elements at the starting of linked list. 
    def prepend(self, element):
        newNode = Node(element)

        if self.head == None:
            self.head = newNode
            newNode.prev = self.head
            newNode.next = self.head
        else:
            # else traverse through last node.
            temp = self.head 
            while (temp.next != self.head):
                temp = temp.next 
            temp.next = newNode
            newNode.prev = temp 
            newNode.next = self.head 
            self.head.prev = newNode
            self.head = newNode 

    # adding elements at the ending of linked list.
    def append(self, element):
        newNode = Node(element)
        if self.head == None:
            self.head = newNode
            newNode.prev = self.head
            newNode.next = self.head
        else:
            # else traverse through last node.
            temp = self.head
            while (temp.next != self.head):
                temp = temp.next 
            temp.next = newNode
            newNode.prev = temp
            newNode.next = self.head 

    # removing elements at the starting of Linked List.
    def delete_at_start(self):
        # the list contains one node, delete and make the head null
        if self.head.next == self.head:
            self.head = None
        else:
            """
            if the list contains more than one node,
            create two nodes - temp and firstNode, both
            pointing to head node
            """
            temp = self.head
            # firstNode = self.head 
            # using temp node, traverse to the last node.
            while (temp.next != self.head):
                temp = temp.next 
            # make head as next of head,
            self.head = self.head.next 
            self.head.prev = temp
            temp.next = self.head 

    # removing elements at the ending of Linked List.
    def delete_at_end(self):
        # the list contains one node, delete and make the head null
        if self.head.next == self.head:
            self.head = None
        else:
            # Else, traverse to the second last element of the list
            temp = self.head 
            while (temp.next.next != self.head):
                temp = temp.next 
            # Update links of head and second last node, and delete the last node
            temp.next = self.head  
            self.head.prev = temp 

    # counting number of nodes in linked list.
    def count_nodes(self):
        # create a temp node pointing to head
        temp = self.head 
        # create a variable to count nodes
        i = 0
        #  if the temp node is not null increase i by 1 and move to the next node, repeat the process till the temp becomes null
        if (temp != None):
            i += 1
            temp = temp.next 
        while (temp != self.head):
            i += 1
            temp = temp.next 
        print("Number of Nodes in Linked List ", i) 

    # delete_all_nodes in linked list
    def delete_all_nodes(self):
        if self.head != None:
            # if head is not null create a temp node and current node pointed to next of head 
            curr = self.head.next 
            while (curr != self.head):
                """
                if current node is not equal to head, delete the current node and move current to next node using temp, repeat the process till the current reaches the head
                """
                curr = curr.next 
            # Delete the head
            self.head = None 
        print("All nodes are deleted successfully.") 

    # reversing the elements in linked list. 
    def reverseList(self):
        # If head is not null create three nodes
        # prevNode - pointing to head,
        # tempNode - pointing to head,
        # curNode - pointing to next of head
        if (self.head != None):
            prevNode = self.head
            tempNode = self.head 
            currNode = self.head.next 

        # assign next and previous of prevNode 
        # as itself to make the first node as 
        # last node of the reversed list
        prevNode.next = prevNode
        prevNode.prev = prevNode 

        while (currNode != self.head):
            # While the curNode is not head adjust links
            # (unlink curNode and link it to the reversed list from front and modify curNode and prevNode) 
            tempNode = currNode.next

            currNode.next = prevNode
            prevNode.prev = currNode
            self.head.next = currNode
            currNode.prev = self.head

            prevNode = currNode
            currNode = tempNode
        
        # Make prevNode (last node) as head
        self.head = prevNode 

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

    def add_at(self, new_element, index):
        # create new node with new element
        # create a temp node to traverse the list
        newnode = Node(new_element)
        temp = self.head 
        no_of_elements = 0

        # finding the number of elements in linked list
        if (temp != None):
            no_of_elements += 1
            temp = temp.next 
        while (temp != self.head):
            no_of_elements += 1
            temp = temp.next 
        
        # check if insertion index is valid.
        if (index < 1 or index > (no_of_elements)):
            print("Invalid index")
        elif (index == 1):
            # if the index is 1, make next of the new node as head and prev of new node as head
            if (self.head == None):
                self.head = newnode
                self.head.next = self.head
                self.head.prev = self.head 
            else:
                while (temp.next != self.head):
                    temp = temp.next 
                temp.next = newnode
                newnode.prev = newnode 
                newnode.next = self.head 
                self.head.prev = newnode 
                self.head = newnode 
        else:
            # Else, traverse to the node previous to the given index, make new node next as temp next and temp next as new node 
            temp = self.head
            for i in range(1, index-1):
                temp = temp.next 
            newnode.next = temp.next 
            # newnode.next.prev = newnode 
            newnode.prev = temp 
            temp.next = newnode 

    def delete_at(self, index):
        #  create two nodes - temp and nodeToDelete 
        #  to traverse and track the node to delete
        node_to_delete = self.head 
        temp = self.head 
        no_of_elements = 0 

        # find the number of elements in the list.
        if (temp != None):
            no_of_elements += 1
            temp = temp.next 
        while (temp != self.head):
            no_of_elements += 1
            temp = temp.next 
        
        # check if the specified index is valid.
        if (index < 1 or index > no_of_elements):
            print("Invalid Position.")
        elif (index == 1):
            # if index is 1 and head is the only element in the list, then make it null, else make next of head as new head and adjust links accordingly
            if (self.head.next == self.head):
                self.head = None 
            else:
                while (temp.next != self.head):
                    temp = temp.next 
                self.head = self.head.next
                temp.next = self.head
                self.head.prev = temp
                node_to_delete = None 
        else:
            # traverse to the node previous to the given position and delete the given node and adjust links accordingly 
            temp = self.head 
            for i in range(1, index -1):
                temp = temp.next 
            node_to_delete = temp.next 
            temp.next = temp.next.next 
            temp.next.prev = temp 
            node_to_delete = None 

    def search_element(self, search_element):
        # create a temp node pointing to head
        temp = self.head
        flag = False
        i = 0 
        # if the temp node is not null check the node value with searchValue, if found update variables and break the loop,  else continue searching till temp node is not head
        if (temp != None):
            while True:
                i += 1
                if (temp.data == search_element):
                    flag = True
                    break 
                temp = temp.next 
                if (temp == self.head):
                    break 
            if (flag == True):
                print(f"{search_element} is found at index = {i}")
            else:
                print(f"{search_element} is not found in the linked list.") 
        else:
            # If the temp node is null at the start, the list is empty
            print("The list is empty.")


list1 = LinkedList()
list1.append(200) 
list1.prepend(10)
list1.prepend(20)
list1.prepend(30) 
list1.append(100)
# list1.print_list()
# list1.count_nodes() 
# list1.delete_at_start()
# list1.print_list()
# list1.delete_at_end()
# list1.print_list() 
# list1.count_nodes()
# list1.delete_all_nodes()
# list1.print_list()
# list1.add_at(101, 5)
# list1.print_list()
# list1.delete_at(2)
list1.print_list()
list1.search_element(202)