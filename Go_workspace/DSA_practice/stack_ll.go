// implementing queue using linked list in Go.

package main

import (
	"fmt"
)

type Node struct{
	data int 
	next *Node 
}

type Stack struct{
	head *Node
	top *Node 
	countNodes int 
}

func (s *Stack) traversal(){
	temp := s.head //temporary pointer to point to head 
	for (temp != nil){ //iterating over stack 
		fmt.Printf("%d ",temp.data)
		temp = temp.next 
	}
	fmt.Println() 
}

func (s *Stack) push(n *Node){
	if s.head == nil && s.top == nil{
		s.head = n 
		s.top = n 
	}else{
		s.top.next = n 
		s.top = n 
	}
	s.countNodes += 1
}

func (s *Stack) pop(){
	if s.head == nil && s.top == nil {
		fmt.Println("Stack is Empty")
	}else{
		temp := s.head 
		for (temp.next != s.top){
			temp = temp.next 
		}
		temp.next = nil 
		s.top = temp 
	}
	s.countNodes -= 1 
}

func (s *Stack) is_empty() bool{
	if (s.head == nil){
		return true 
	}
	return false 
}

func (s *Stack) peek() int{
	if s.head == s.top{
		fmt.Println("Stack is Empty.")
		return -1 
	}else{
		e := s.top.data 
		return e 
	}
}

func (s *Stack) get_size() int{
	return s.countNodes
}

func main(){
	s := Stack{}
	node1 := &Node{data: 10}
	node2 := &Node{data: 20}
	node3 := &Node{data: 30}
	fmt.Println(s.get_size()) 
	s.push(node1)
	s.push(node2)
	s.push(node3)
	s.traversal()
	fmt.Println(s.get_size())
	fmt.Println(s.peek())
	s.pop()
	fmt.Println(s.get_size())
	s.traversal()
	fmt.Println(s.is_empty())
	fmt.Println(s.peek())
}


