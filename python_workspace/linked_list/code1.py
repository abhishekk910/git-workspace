# node structure 
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

linked_list = Linked_List()
linked_list.print_list() 
linked_list.prepend(20)
linked_list.append(10)
linked_list.prepend(30)
linked_list.prepend(40)
linked_list.print_list()
linked_list.remove_at_first()
linked_list.remove_at_last()
linked_list.print_list()