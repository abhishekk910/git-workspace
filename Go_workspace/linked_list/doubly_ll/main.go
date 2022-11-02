package main 

import "fmt"

//creating node
type node struct{
	data int 
	next *node 
	prev *node 
}

// creating circular Doubly linked list 
type circularDoublyLinkedList struct{
	head *node 
	length int 
}

// prepend method adds element at the front of the linked list. 
func (cdll *circularDoublyLinkedList) prepend(newNode *node){
	if cdll.head == nil{
		cdll.head = newNode
		newNode.prev = cdll.head
		newNode.next = cdll.head
	}else{
		//# else traverse through last node.
		temp := cdll.head 
		for(temp.next != cdll.head){
			temp = temp.next
		}
		temp.next = newNode 
		newNode.prev = temp 
		newNode.next = cdll.head 
		cdll.head.prev = newNode 
		cdll.head = newNode 
	}
}

// append method adds element at the end of the linked list.
func (cdll *circularDoublyLinkedList) append(newNode *node){
	if cdll.head == nil {
		cdll.head = newNode
		newNode.prev = cdll.head 
		newNode.next = cdll.head 
	}else{
		// else traverse through last node.
		temp := cdll.head 
		for (temp.next != cdll.head){
			temp = temp.next 
		}
		temp.next = newNode
		newNode.prev = temp 
		newNode.next = cdll.head 
	}
}



// tarversal method
func (cdll *circularDoublyLinkedList) print_list(){
	temp := cdll.head 
	if (temp != nil){
		for true{
			fmt.Printf("%d ",temp.data)
			temp = temp.next 
			if (temp == cdll.head){
				break 
			}
		}
		fmt.Println() 
	}else{
		fmt.Println("The Linked list is empty..")
	}
}

// deleting element at the front of linked list.
func (cdll *circularDoublyLinkedList) delete_at_start(){
	// the list contains one node, delete and make the head null
	if (cdll.head.next == nil){
		cdll.head = nil 
	}else{
		//if the list contains more than one node,
		//create two nodes - temp and firstNode, both
		//pointing to head node
		temp := cdll.head 
		// firstNode = self.head 
		// using temp node, traverse to the last node.
		for (temp.next != cdll.head){
			temp = temp.next 
		}
		// make head as next of head,
		cdll.head = cdll.head.next 
		cdll.head.prev = temp 
		temp.next = cdll.head 
	}
}

// deleting element at the ending of linked list.
func (cdll *circularDoublyLinkedList) delete_at_end(){
	// the list contains one node, delete and make the head null
	if (cdll.head.next) == cdll.head{
		cdll.head = nil 
	}else{
		// Else, traverse to the second last element of the list
		temp := cdll.head 
		for (temp.next.next != cdll.head){
			temp = temp.next 
		}
		// Update links of head and second last node, and delete the last node
		temp.next = cdll.head 
		cdll.head.prev = temp 
	}
}

//counting number of nodes in linked list.
func (cdll *circularDoublyLinkedList) count_nodes(){
	// create a temp node pointing to head
	temp := cdll.head 
	// create a variable to count nodes
	i := 0 
	// if the temp node is not null increase i by 1 and move to the next node, repeat the process till the temp becomes nil
	if (temp != nil){
		i += 1
		temp = temp.next 
	}
	for (temp != cdll.head){
		i += 1
		temp = temp.next 
	}
	fmt.Println("Number of Nodes in Linked List", i) 
}

// delete_all_nodes in linked list
func (cdll *circularDoublyLinkedList) delete_all_nodes(){
	if (cdll.head != nil){
		//  if head is not null create a temp node and current node pointed to next of head 
		curr := cdll.head.next 
		for (curr != cdll.head){
			//if current node is not equal to head, delete the current node and move current to next node using temp
			// repeat the process till the current reaches the head
			curr = curr.next 
		}
		// delete the head 
		cdll.head = nil 
	}
	fmt.Println("All nodes are deleted successfully.") 
}

//reversing the elements in linked list. 
func (cdll *circularDoublyLinkedList) reverseList(){
	// If head is not null create three nodes
	// prevNode - pointing to head,
	// tempNode - pointing to head,
	// curNode - pointing to next of head
	if (cdll.head != nil){
		prevNode := cdll.head
		tempNode := cdll.head 
		currNode := cdll.head.next 
	
	//assign next and previous of prevNode 
	//as itself to make the first node as 
	//last node of the reversed list
		prevNode.next = prevNode
		prevNode.prev = prevNode 

		for (currNode != cdll.head){
			//While the curNode is not head adjust links
			// (unlink curNode and link it to the reversed list from front and modify curNode and prevNode) 
			tempNode = currNode.next

			currNode.next = prevNode
			prevNode.prev = currNode
			cdll.head.next = currNode
			currNode.prev = cdll.head

			prevNode = currNode
			currNode = tempNode
		}
	// Make prevNode (last node) as head
	cdll.head = prevNode 
	}	
}

// sorting the elements in ascending order
func(cdll *circularDoublyLinkedList) sortList(){
	if cdll.head == nil{
		fmt.Println("Linked list is Empty..")
	}else{
	// Current will point to head 
	curr := cdll.head 
	for true{
		index := curr.next
		for (index != cdll.head){
			// If current node is greater than index data, swaps the data 
			if (curr.data > index.data){
				curr.data, index.data = index.data, curr.data
			}
			index = index.next
		}
		curr = curr.next
		if (curr.next == cdll.head){
			break 
		}
	}
	}
}

func main(){
	ll := circularDoublyLinkedList{}
	node1 := &node{data: 10}
	node2 := &node{data: 20} 
	node3 := &node{data: 30}
	node4 := &node{data: 40}
	ll.prepend(node3)
	ll.append(node4)
	ll.append(node1)
	ll.prepend(node2)   
	ll.print_list()
	ll.sortList()
	ll.print_list()
	//ll.delete_all_nodes()
	//ll.print_list()
	// ll.print_list()
	// ll.count_nodes()
	// ll.delete_at_start()
	// ll.print_list()
	// ll.delete_at_end()
	// ll.print_list()
	// ll.count_nodes()
	// ll.reverseList()
	// ll.print_list()
} 