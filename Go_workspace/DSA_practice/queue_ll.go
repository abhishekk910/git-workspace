// implementing stack using linked list in Go.

package main

import (
	"fmt"
)

type Node struct{
	data int 
	next *Node 
}

type Queue struct{
	head *Node 
	tail *Node
	nodesCount int 
}

func (q *Queue) traversal(){
	temp := q.head // temporary pointer to point to head
	for (temp != nil){
		fmt.Printf("%d ", temp.data)
		temp = temp.next 
	}
	fmt.Println() 
}

func (q *Queue) enqueue(n *Node){
	if q.head == nil && q.tail == nil{
		q.head = n 
		q.tail = n 
	}else{
		q.tail.next = n 
		q.tail = n 
	}
	q.nodesCount += 1 
}

func (q *Queue) dequeue(){
	if q.head == nil && q.tail == nil{
		fmt.Println("Queue is Empty") 
	}else{
		q.head = q.head.next 
	}
	q.nodesCount -= 1
}

func (q *Queue) peek() int{
	if q.head == nil{
		return -1 
	}
	return q.head.data 
}

func (q *Queue) is_empty() bool{
	if (q.head == nil && q.tail == nil){
		return true 
	}
	return false 
}

func (q *Queue) get_size() int{
	return q.nodesCount 
}

func main(){
	q := Queue{}
	node1 := &Node{data: 10}
	node2 := &Node{data: 20}
	node3 := &Node{data: 30}
	q.enqueue(node1)
	q.enqueue(node2)
	q.enqueue(node3) 
	q.traversal()
	fmt.Println(q.get_size())
	q.dequeue()
	q.traversal()
	fmt.Println(q.get_size())
	fmt.Println(q.peek())
}

