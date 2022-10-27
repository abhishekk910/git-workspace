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

func (dll *doublylinkedlist) sort(){
	if (dll.head == nil){
		fmt.Println("Linked List is Empty.")
	}else{
		curr := dll.head 
		for (curr.next != nil){
			index := curr.next 
			for (index != nil){
				if (curr.data > index.data){
					index.data, curr.data = curr.data, index.data
				}
				index = index.next
			}
			curr = curr.next
		}
	}
}

func (dll *doublylinkedlist) push_at(data int, index int){
	new_node := &node{}
	new_node.data = data 
	new_node.prev = nil
	new_node.next = nil 
	if index < 1{
		fmt.Println("Index value should be greater than 1")
	}else if (index == 1){
		new_node.next = dll.head
		dll.head = new_node 
	}else{
		temp := dll.head 
		for i:=1; i < index-1; i++{
			if (temp != nil){
				temp = temp.next 
			}
		}
		if (temp != nil){
			new_node.next = temp.next 
            new_node.prev = temp 
            temp.next = new_node
			if (new_node.next != nil){
				new_node.next.prev = new_node
			}else{
				fmt.Println("The previous node is null.")
			}
		}
	}
}

func (dll *doublylinkedlist) pop_at(index int){
	if (index < 1){
		fmt.Println("Index value should be greater than 1")
	}else if (index == 1){
		dll.head = dll.head.next 
	}else{
		temp := dll.head 
		for i:=1; i < index-1; i++{
			if (temp != nil){
				temp = temp.next 
			}
		}
		if (temp != nil && temp.next != nil){
			//node_to_delete := temp.next 
			temp.next = temp.next.next 
			if (temp.next.next != nil){
				temp.next.next.prev = temp.next 
			}
			//node_to_delete = nil 
		}else{
			fmt.Println("The node is null.") 
		}
	}
}

func (dll doublylinkedlist) count_nodes(){
	temp := dll.head 
	count := 0
	for (temp != nil){
		count += 1
		temp = temp.next 
	}
	fmt.Printf("Number of nodes : %d", count) 
}

func (dll *doublylinkedlist) delete_all_nodes(){
	for (dll.head != nil){
		dll.head = dll.head.next
	}
	fmt.Println("All nodes deleted successfully..")
}

func (dll doublylinkedlist) search_element(search_value int){
	temp := dll.head 
	flag := false
	i := 0
	if (temp != nil){
		for (temp != nil){
			i += 1
			if (temp.data == search_value){
				flag = true 
				break 
			}
			temp = temp.next 
		}
		if (flag == true){
			fmt.Printf("%d is found at index %d", search_value, i)
		}else{
			fmt.Printf("%d is not found in the list.", search_value) 
		}
	}else{
		fmt.Println("The list is empty.")
	}
}

func main(){
	mylist := doublylinkedlist{}
	mylist.append(10)
	mylist.prepend(30) 
	mylist.append(20)
	// mylist.display()
	mylist.sort()
	// mylist.display()
	//mylist.reversedisplay()
	mylist.push_at(100, 2) 
	mylist.display()
	//mylist.pop_at(1) 
	mylist.display()
	//mylist.count_nodes()
	// mylist.delete_all_nodes()
	// mylist.display()
	mylist.search_element(100)
}
