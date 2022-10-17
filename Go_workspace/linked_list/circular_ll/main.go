package main

import "fmt"

// creating node 
type node struct{
	value int 
	next *node 
}

// creating circular singly linked list 
type circularSinglyLinkedList struct{
	head *node 
	length int 
}

// prepend method adds element at the front of the linked list. 
func (ll *circularSinglyLinkedList) prepend(n *node) {
	if ll.head == nil{
		ll.head = n 
		n.next = ll.head 
		return 
	}else{
		temp := ll.head
		for (temp.next != ll.head){
			temp = temp.next 
		}
		temp.next = n 
		n.next = ll.head 
		ll.head = n 
	}
	ll.length++
}

// prepend method adds element at the end of the linked list.
func (ll *circularSinglyLinkedList) append(n *node){
	if ll.head == nil{
		ll.head = n 
		n.next = ll.head 
	}else{
		temp := ll.head 
		for (temp.next != ll.head){
			temp = temp.next 
		}
		temp.next = n  //current last node pointing to new node.
		n.next = ll.head  // new last node pointing to head 
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
func (ll circularSinglyLinkedList) display(){
	if ll.head != nil {
        fmt.Print(ll.head.value, " ")
        if ll.head.next != nil {
            for cur := ll.head.next; cur != ll.head; cur = cur.next {
                fmt.Print(cur.value, " ")
            }
			fmt.Println()
        }
    }else{
		fmt.Println("Linked List is Empty..")
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

func main(){
	ll := circularSinglyLinkedList{}
	node1 := &node{value: 10}
	node2 := &node{value: 20} 
	node3 := &node{value: 30}
	node4 := &node{value: 40}
	ll.prepend(node2)
	ll.append(node3)
	ll.append(node4)
	ll.prepend(node1)  
	ll.display()
	ll.countNodes()
	ll.deleteAtStart()
	ll.display()
	ll.countNodes()
	ll.deleteAtEnd()
	ll.display()
	ll.countNodes()
	ll.deleteAllNodes()
	ll.display()
	ll.countNodes()
}