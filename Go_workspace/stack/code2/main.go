// Implementation of stack in Go

package main

import "fmt"

type Stack struct{
	elements []int 
}

// Push method is used to append elements to the end of stack. 
func (s *Stack) Push(i int){
	s.elements = append(s.elements, i) 
	fmt.Printf("Element %d to stack\n", i)
}

// Pop method will remove the last element and returns element from stack.
func (s *Stack) Pop(){
	l := len(s.elements) - 1
	removedElement := s.elements[l]
	s.elements = s.elements[:l]
	fmt.Printf("%d removed from stack\n", removedElement)
}

// Peek Method is used to get top element from stack.
func (s *Stack) Peek(){
	if len(s.elements) > 0{
		e := len(s.elements)-1
		fmt.Printf("Top Element is %d\n", s.elements[e])
	}else{
		fmt.Println("Stack is Empty")
	}
}

// isEmpty method return true when length of stack is zero.
func (s *Stack) isEmpty(){
	if len(s.elements) == 0{
		fmt.Println("Length of Stack is Zero..")
	}else{
		fmt.Printf("Length of Stack is %d", len(s.elements))
	}
}

func main(){
	mystack := Stack{}
	fmt.Println(mystack)
	mystack.isEmpty()
	mystack.Push(10)
	mystack.Push(20)
	mystack.Push(30)
	fmt.Println(mystack)
	mystack.Peek()
	mystack.Pop()
	mystack.Push(40)
	fmt.Println(mystack)
}