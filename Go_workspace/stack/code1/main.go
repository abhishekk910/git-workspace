package main

import (
	"fmt"
)

type Stack struct {
	elements []int
}

// push method will add element to the end of the stack
func (s *Stack) Push(i int) {
	s.elements = append(s.elements, i)
}

// pop method will remove the last element and returns that element from stack
func (s *Stack) Pop(){
	l := len(s.elements) - 1 
	removedElement := s.elements[l]
	s.elements = s.elements[:l]
	fmt.Printf("%d removed from stack\n", removedElement) 
}

// Peek method is used to get top element from stack. 
func (s *Stack) Peek(){
	if len(s.elements) > 0{
		e := len(s.elements)-1
		fmt.Printf("Top element is %d\n", s.elements[e])
	}else{
		fmt.Println("Stack is Empty")
	}
}

// isEmpty method return true when length of stack is zero. 
func (s *Stack) isEmpty() bool{
	return len(s.elements) == 0
}

func main() {
	myStack := Stack{}
	fmt.Println(myStack)
	myStack.Push(10)
	myStack.Push(20)
	myStack.Push(30)
	fmt.Println(myStack)
	myStack.Peek()
	myStack.Pop()
	fmt.Println(myStack)
	myStack.Pop()
	fmt.Println(myStack)
	fmt.Println("Stack length is empty : ",myStack.isEmpty())
	myStack.Peek()
	myStack.Pop()
	fmt.Println("Stack length is empty : ",myStack.isEmpty())
}
