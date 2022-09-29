package main

import (
	"fmt"
)

type Queue struct {
	elements []int
}

// enqueue method adding an element at the end of queue
func (q *Queue) Enqueue(i int){
	q.elements = append(q.elements, i)
}

// dequeue method :- removing the front item from Queue
func (q *Queue) Dequeue(){
	e := q.elements[0]
	q.elements = q.elements[1:]
	fmt.Printf("%d removed from Queue\n", e) 
}

// isEmpty method return true when length of queue is zero. 
func (q *Queue) isEmpty() bool{
	return len(q.elements) == 0
}

// First method is used to get first element from queue.
func (q *Queue) First(){
	if len(q.elements) == 0{
		fmt.Println("Queue is Empty")
	}else{
		fmt.Println("First Element :", q.elements[0]) 
	}
}

func main(){
	myQueue := Queue{}
	myQueue.Enqueue(10)
	myQueue.Enqueue(20)
	myQueue.Enqueue(30)
	fmt.Println(myQueue.elements) 
	myQueue.First()
	myQueue.Dequeue()
	fmt.Println(myQueue.isEmpty())
	fmt.Println(myQueue.elements) 
	myQueue.First()
	myQueue.Dequeue()
	fmt.Println(myQueue.elements) 
	myQueue.Dequeue()
	fmt.Println(myQueue.elements) 
	fmt.Println(myQueue.isEmpty())
	myQueue.First()
}