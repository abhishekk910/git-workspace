package main

import "fmt"

type node struct {
	data int
	prev *node
	next *node
}

type doublylinkedlist struct {
	len  int
	head *node
	tail *node
}

func (dll *doublylinkedlist) append(num int) {
	temp := &node{}
	temp.data = num
	temp.next = nil
	temp.prev = nil
	if dll.head == nil && dll.tail == nil {
		dll.head = temp
		dll.tail = temp
	} else {
		temp.prev = dll.tail
		dll.tail.next = temp
		dll.tail = temp
	}
	dll.len++
}

func (dll *doublylinkedlist) prepend(num int){
	temp := &node{}
	temp.data = num 
	temp.prev = nil
	temp.next = nil 
	if dll.head == nil && dll.tail == nil{
		dll.head = temp 
		dll.tail = temp 
	}else{
		temp.next = dll.head 
		dll.head.prev = temp
		dll.head = temp 
	}
	dll.len++ 
}

func (dll *doublylinkedlist) deleteAtFirst(){
	if dll.head == nil{
		fmt.Println("Linked list is empty..")
	}else{
		dll.head = dll.head.next 
	}
	dll.len--
}

func (dll *doublylinkedlist) deleteAtLast(){
	if dll.tail.prev == nil{
		fmt.Println("Linked List is empty.")
	}else{
		dll.tail = dll.tail.prev  
		dll.tail.next = nil 
	}
	dll.len-- 
}

func (dll doublylinkedlist) display() {
	e := dll.head
	for e != nil {
		fmt.Printf("%d ->", e.data) 
		e = e.next 
	}
	fmt.Printf("Nil\n") 
}

func (dll doublylinkedlist) reversedisplay() {
	e := dll.tail 
	for e != nil {
		fmt.Printf("%d ->", e.data) 
		e = e.prev  
	}
	fmt.Printf("Nil\n")
}

func main(){
	mylist := doublylinkedlist{}
	mylist.append(10)
	mylist.append(20)
	mylist.append(30)
	mylist.prepend(40)
	mylist.append(50) 
	mylist.display()
	// mylist.reversedisplay()
	mylist.deleteAtFirst()
	mylist.display()
	mylist.deleteAtLast()
	mylist.display()
}

