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





list1 = LinkedList()
list1.append(200) 
list1.prepend(10)
list1.prepend(20)
list1.prepend(30) 
list1.append(100)
list1.print_list()
# list1.count_nodes() 
# list1.delete_at_start()
# list1.print_list()
# list1.delete_at_end()
# list1.print_list() 
# list1.count_nodes()
# list1.delete_all_nodes()
# list1.print_list()
list1.reverseList()
list1.print_list()
list1.sortList()
list1.print_list()