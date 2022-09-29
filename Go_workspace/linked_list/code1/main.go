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
	mylist.lengthOfLinkedList() 
	mylist.removeAtLast()
	mylist.printList()
	mylist.removeAtFront()
	mylist.printList() 
	mylist.lengthOfLinkedList() 
}
