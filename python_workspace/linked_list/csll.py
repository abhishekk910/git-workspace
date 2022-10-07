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
                print(f"{temp.data} ", end="")
                temp = temp.next 
                if (temp == self.head):
                    break 
            print()
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
            new_node.next = self.head  #current 1st node to 2nd node
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

list1 = Circular_Linked_List()
# list1.print_list()
# first = Node(10)
# list1.head = first 
# first.next = first 

# second = Node(20)
# first.next = second
# second.next = list1.head

# third = Node(30)
# second.next = third 
# third.next = list1.head
# list1.print_list()


list1.prepend(20)
list1.append(30) 
list1.append(40)
list1.prepend(10)
list1.print_list() 
list1.count_nodes()
list1.delete_at_start()
list1.print_list()
list1.count_nodes()  
list1.delete_at_end()
list1.print_list() 
list1.count_nodes() 
list1.delete_all_nodes()
list1.print_list() 
list1.count_nodes()