package main

import "fmt"

// node contains data and reference of next node 
type node struct{
	data int
	next *node 
}

// head of pointer to node and length.
type linkedlist struct{
	head *node 
	length int 
}

// prepend method adds element at the front of the linked list. 
func (l *linkedlist) prepend(n *node){
	current := l.head
	l.head = n 
	l.head.next = current
	l.length++ 
}

// append method adds element at the end of the linked list
func (l *linkedlist) append(n *node){
	if l.head == nil{
		l.head = n 
	}else{
		current := l.head 
		for current.next != nil{
			current = current.next
		}
		current.next = n 
	}
	l.length++ 
}

// printing the elements in linkedlist
func (l linkedlist) printList(){
	temp := l.head	
	for l.length != 0{
		fmt.Printf("%d->", temp.data)
		temp = temp.next 
		l.length-- 
	}
	fmt.Printf("Nil\n")
}

// Removing element at the front of linked list
func (l *linkedlist) removeAtFront(){
	if l.head == nil{
		fmt.Println("Linked List is Empty")
		return 
	}
	l.head = l.head.next
	l.length--
}

// Removing element at the end of linked list
func (l *linkedlist) removeAtLast(){
	if l.head == nil{
		fmt.Println("Linked List is Empty")
		return 
	}
	var prev *node
	current := l.head
	for current.next != nil{
		prev = current 
		current = current.next 
	}
	if prev != nil{
		prev.next = nil 
	}else{
		l.head = nil 
	}
	l.length--
}

func (l linkedlist) lengthOfLinkedList(){
	fmt.Println("Length of Linked List :", l.length)
}

func (l *linkedlist) reverseList(){
	if (l.head != nil){
		prevNode := l.head //prevnode pointing to head
		tempNode := l.head // pointing to head 
		currNode := l.head.next //pointing to next of head
		// assign next of prevNode as null to make the
		// first node as last node of the reversed list
		prevNode.next = nil 
		for (currNode != nil){
			//  While the curNode is not null adjust links 
			// (unlink curNode and link it to the reversed list 
        	// from front and modify curNode and prevNode)
			tempNode = currNode.next 
			currNode.next = prevNode 
			prevNode = currNode 
			currNode = tempNode 
		}
		// make prevnode (last node) as head
		l.head = prevNode 
	}
}

// sorting the elements in Linked List 
func (l *linkedlist) sort_list(){
	curr := l.head 
	//index := nil 
	if (l.head == nil){
		fmt.Println("Linked List is Empty..")
		return 
	}else{
		for (curr != nil){
			// node index will point to node next to current
			index := curr.next 
			for (index != nil){
				if (curr.data > index.data){
					temp := curr.data
					curr.data = curr.next.data 
					index.data = temp 
				}
				index = index.next
			}
			curr = curr.next 
		}
	}
}

//searching for a element in Linked List.
func (l *linkedlist) search_element(n int){
	// create a temp node pointing to node. 
	temp := l.head 
	flag := false 
	i := 0
	/*
	if the temp node is not null check the
        node value with searchValue, if found 
        update variables and break the loop, else
        continue searching till temp node is not null 
	*/
	if (temp != nil){
		for (temp != nil){
			i += 1 
			if (temp.data == n){
				flag = true 
				break 
			}
			temp = temp.next 
		}
		if (flag == true){
			fmt.Printf("%d is found at index number %d\n", n, i)
		}else{
			fmt.Println("search element did not found..")
		}
	}
}

// adding value at the index value.
func (l *linkedlist) push_at(new_number int, index int){
	newNode := node{data : new_number} 
	if (index < 1){
		fmt.Println("index should be greater than 0")
	}else if(index == 1){
		newNode.next = l.head 
		l.head = &newNode 
	}else{
		temp := l.head 
		for i := 1; i < index-1;i++{
			if (temp != nil){
				temp = temp.next 
			}
		}
		/*
		If the previous node is not null, make 
        newNode next as temp next and temp next 
        as newNode.
		*/
		if (temp != nil){
			newNode.next = temp.next 
			temp.next = &newNode 
		}else{
			fmt.Println("Previous node is null..")
		}
	}
}

//removing element from the list by index number.
func (l *linkedlist) pop_at(index int){
	if (index < 1){
		fmt.Println("index should be greater than 0")
	}else if(index == 1){
		l.head = l.head.next
	}else{
		/* 
		Make  a temp node and traverse to the temp previous to the position.
		*/
		temp := l.head 
		for i:=1; i< (index-1); i++{
			if (temp != nil){
				temp = temp.next 
			}
		}
		if (temp != nil && temp.next != nil){ 
			temp.next = temp.next.next  
		}else{
			fmt.Println("The node is null.")
		}
	}
}

func main(){
	mylist := linkedlist{}
	node1 := &node{data:10}
	node2 := &node{data:20}
	node3 := &node{data:30}
	node4 := &node{data:40}
	node5 := &node{data:50} 
	mylist.prepend(node1)
	mylist.prepend(node2)
	mylist.append(node3)
	mylist.prepend(node4)  
	mylist.prepend(node5) 
	mylist.printList()
	// mylist.lengthOfLinkedList() 
	// mylist.removeAtLast()
	// mylist.printList()
	// mylist.removeAtFront()
	// mylist.printList() 
	// mylist.lengthOfLinkedList() 
	mylist.reverseList()
	mylist.printList()
	mylist.sort_list()
	mylist.printList() 
	mylist.search_element(30)
	mylist.push_at(101, 6)
	mylist.printList()
	mylist.lengthOfLinkedList()
	mylist.pop_at(3)
	mylist.printList()
}
