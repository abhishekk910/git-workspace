// Implementation of queue in Go

package main

import "fmt"

type Queue struct{
	elements []int
	maxSize int 
}

// Enqueue method is used to add element at the end of queue.
func (q *Queue) enqueue(i int){
	l := len(q.elements)
	if q.maxSize == l{
		fmt.Println("Queue Size is Full")
	}else{
		q.elements = append(q.elements, i)
		fmt.Printf("%d appended to stack\n", i) 
	}
}

// Deque method is used to remove first element from the queue.
func (q *Queue) dequeue(){
	e := q.elements[0]
	q.elements = q.elements[1:]
	fmt.Println(q.elements)
	fmt.Printf("%d is removed from stack\n", e) 
}

// Gets the element at the front of the queue without removing it.
func (q *Queue) peek(){
	e := q.elements[0]
	fmt.Printf("%d is present at the front of queue.\n", e)
}

// Checks if the queue is full.
func (q *Queue) isFull(){
	if q.maxSize == len(q.elements){
		fmt.Println("SIze of Queue is Full.")
	}
}

// Checks if the queue is empty.
func (q *Queue) isEmpty(){
	if len(q.elements) == 0{
		fmt.Println("Size of Queue is Zero.")
	}
}

func main(){
	myqueue := Queue{maxSize: 4}
	myqueue.enqueue(10)
	myqueue.enqueue(20)
	myqueue.enqueue(30)
	myqueue.isEmpty()
	myqueue.enqueue(40)
	fmt.Println(myqueue.elements) 
	myqueue.isEmpty()
	myqueue.dequeue()
	myqueue.peek()
	fmt.Println(myqueue.elements)
}