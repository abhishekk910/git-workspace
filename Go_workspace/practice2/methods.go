package main 

import "fmt"

// type employee struct{
// 	name string
// 	loc string
// 	id int 
// }

// func (e employee) display(){
// 	fmt.Println(e.name, e.id, e.loc) 
// }

// func main(){
// 	e1 := employee{
// 		name: "Abhshek",
// 		loc: "Bangalore",
// 		id: 1000,
// 	}
// 	e1.display()
// }

// type num int 

// func (n1 num)product(n2 num)num{
// 	return n1 * n2 
// }

// func main(){
// 	n1 := num(10)
// 	n2 := num(20)
// 	res := n1.product(n2)
// 	fmt.Println(res) 
// }


// type employee struct{
// 	name, loc string
// 	id int 
// }

// func (e *employee) display(loc1 string){
// 	(*e).loc = loc1 
// }

// func main(){
// 	e1 := employee{
// 		name : "ABC",
// 		loc : "Bangalore",
// 		id : 1111,
// 	}
// 	fmt.Println(e1.name, e1.loc)

// 	p:= &e1 

// 	p.display("Chennai")
// 	fmt.Println(e1.name, e1.loc)
// }


// type employee struct{
// 	name, loc string
// 	id int 
// }

// func (e *employee) display1(loc1 string){
// 	(*e).loc = loc1 
// }

// func (e employee) display2(){
// 	e.name = "ABC" 
// }

// func main(){
// 	e1 := employee{
// 		name : "Abhishek",
// 		loc : "Bangalore",
// 		id : 1000,
// 	}

// 	fmt.Println(e1) 
// 	e1.display1("Mysore")
// 	e1.display2()
// 	fmt.Println(e1) 
// }



