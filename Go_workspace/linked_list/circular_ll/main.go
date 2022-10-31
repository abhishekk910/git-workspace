package main

import "fmt"

// creating node 
type node struct{
	data int 
	next *node 
}

// creating circular singly linked list 
type circularSinglyLinkedList struct{
	head *node 
	length int 
}

// prepend method adds element at the front of the linked list. 
func (csll *circularSinglyLinkedList) prepend(newNode *node) {
	if csll.head == nil{
		csll.head = newNode 
		newNode.next = csll.head 
		return 
	}else{
		temp := csll.head
		for (temp.next != csll.head){
			temp = temp.next 
		}
		temp.next = newNode 
		newNode.next = csll.head 
		csll.head = newNode
	}
	csll.length++
}

// prepend method adds element at the end of the linked list.
func (ll *circularSinglyLinkedList) append(new_node *node){
	if ll.head == nil{
		ll.head = new_node 
		new_node.next = ll.head 
	}else{
		temp := ll.head 
		for (temp.next != ll.head){
			temp = temp.next 
		}
		temp.next = new_node  //current last node pointing to new node.
		new_node.next = ll.head  // new last node pointing to head 
	}
	ll.length++
}

// deleting element at the front of linked list.
func(ll *circularSinglyLinkedList) deleteAtStart(){
	if ll.head == nil{
		fmt.Println("Linked List is Empty..")
		return 
	}else{
		if (ll.head.next == ll.head){
			ll.head = nil 
		}else{
			temp := ll.head 
			for (temp.next != ll.head){
				temp = temp.next
			}
			ll.head = ll.head.next //Make head as next of head(pointing to current 2nd Node)
			temp.next = ll.head // make next of last node pointing to head
		}
	}
	ll.length--
}

// deleting element at the ending of linked list.
func(ll *circularSinglyLinkedList) deleteAtEnd(){
	if (ll.head == nil){
		fmt.Println("Linked List is Empty..")
		return 
	}else{
		if(ll.head.next == ll.head){
			ll.head = nil 
		}else{
			temp := ll.head 
			for (temp.next.next != ll.head){
				temp = temp.next 
			}
			temp.next = ll.head //making last 2nd node to point towards to head node , deleting last node. 
		}
	}
	ll.length--
}

// traversal of linked list
func (ll circularSinglyLinkedList) print_list(){
	if ll.head != nil {
        fmt.Print(ll.head.data, " ")
        if ll.head.next != nil {
            for cur := ll.head.next; cur != ll.head; cur = cur.next {
                fmt.Print(cur.data, " ")
            }
			fmt.Println()
        }
    }else{
		fmt.Println("Linked List is Empty..")
	}
}

//sorting the elements in ascending order
func (csll *circularSinglyLinkedList) sort(){
	if (csll.head == nil){
		fmt.Println("Linked List is Empty.")
	}else{
		curr := csll.head  // Current will point to head
		for true{
			index := curr.next 
			for (index != csll.head){
				// If current node is greater than index data, swaps the data
				if (curr.data > index.data){
					index.data, curr.data = curr.data, index.data
				}
				index = index.next
			}
			curr = curr.next
			if (curr.next == csll.head){
				break 
			}
		}
	}
}

// counting number of nodes in linked list.
func (ll *circularSinglyLinkedList) countNodes(){
	temp := ll.head 
	i := 0
	if (temp != nil){
		for (true){
			temp = temp.next 
			i++
			if (temp == ll.head){
				break 
			}
		}
	}
	fmt.Println("Number of nodes in linked list : ", i) 
}

// deleting all nodes from linked list.
func (ll *circularSinglyLinkedList) deleteAllNodes(){
	if (ll.head == nil){
		fmt.Println("Linked List is Empty.")
	}else{
		if (ll.head.next == ll.head){ //if there is only one node, point head to None 
			ll.head = nil 
		}else{
			curr := ll.head 
			for (curr != ll.head){
				temp := curr.next //store current next in temp. 
				curr = nil  // delete current node. 
				curr = temp // move current to next using temp, repeating the process till current reaches the head.
			}
			ll.head = nil // delete the head. 
		}
	}
}

//reversing the elements in linked list 
func (csll *circularSinglyLinkedList) reverseList(){
	//If head is not null create three nodes
	// prevNode - pointing to head,
	// tempNode - pointing to head,
	// currNode - pointing to next of head
	if (csll.head != nil){
		prev_node := csll.head 
		temp_node := csll.head 
		curr_node := csll.head.next 

		// 2. assign next of prevNode as itself to make the
		// first node as last node of the reversed list
		prev_node.next = prev_node 

		for (curr_node != csll.head){
			//3. While the curNode is not head adjust links 
			// (unlink curNode and link it to the reversed list
			//  from front and modify curNode and prevNode) 
			temp_node = curr_node.next 
			curr_node.next = prev_node
			csll.head.next = curr_node
			prev_node = curr_node 
			curr_node = temp_node 
		}
		//4. Make prevNode (last node) as head
		csll.head = prev_node
	}
}

func (csll *circularSinglyLinkedList) push_at(element int, index int){
	new_node := &node{data: element}
	new_node.next = nil 
	temp := csll.head
	no_of_elements := 0

	//find number of elements
	if (temp != nil){
		no_of_elements += 1
		temp = temp.next 
	}
	for (temp != csll.head){
		no_of_elements += 1
		temp = temp.next 
	}

	// check if adding index is valid
	if (index < 1 || index > (no_of_elements)){
		fmt.Println("Invalid Index")
	}else if (index == 1){
		// if index is 1, make next of new node as head and new node as head 
		if (csll.head == nil){
			csll.head = new_node
			new_node.next = csll.head 
		}else{
			for (temp.next != csll.head){
				temp = temp.next 
			}
			new_node.next = csll.head 
			csll.head = new_node 
			temp.next = csll.head 
		}
	}else{
		temp := csll.head 
		for i := 1; i < (index - 1); i++{
			temp = temp.next
		}
		new_node.next = temp.next 
		temp.next = new_node 
	}
}

func (csll *circularSinglyLinkedList) pop_at(index int){
	//creating two nodes temp and nodeToDelete to traverse and track the node to delete
	//nodeToDelete := csll.head 
	temp := csll.head 
	no_of_elements := 0

	// find the number of elements in the list.
	if (temp != nil){
		no_of_elements += 1
		temp = temp.next 
	}
	for (temp != csll.head){
		no_of_elements += 1
		temp = temp.next 
	}

	// check if specified index is valid.
	if (index < 1 || index > (no_of_elements)){
		fmt.Println("Invalid Index")
	}else if(index == 1){
		// if the index is 1 and head is the only element in the list, make it null,else make next of head as new head and adjust links accordingly.
		if (csll.head.next == csll.head){
			csll.head = nil 
		}else{
			for (temp.next != csll.head){
				temp = temp.next 
			}
			csll.head = csll.head.next 
			temp.next = csll.head 
			//nodeToDelete = nil  
		}
	}else{
		// Else, traverse to node previous to the given index and delete the given node and adjust links accordingly.
		temp := csll.head 
		for i := 0; i < (index - 1); i++{
			temp = temp.next 
		}
		//nodeToDelete := temp.next 
		temp = temp.next 
		//nodeToDelete = nil 
	}
}

func main(){
	ll := circularSinglyLinkedList{}
	node1 := &node{data: 10}
	node2 := &node{data: 20} 
	node3 := &node{data: 30}
	node4 := &node{data: 40}
	ll.append(node2)
	ll.prepend(node3)
	ll.prepend(node4)
	ll.append(node1)  
	ll.print_list()
	// ll.countNodes()
	// ll.deleteAllNodes()
	// ll.print_list()
	ll.push_at(100, 4)
	ll.print_list()
	ll.pop_at(1)
	ll.print_list()
}