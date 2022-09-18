package main

import "fmt"

// func main() {
// 	// declare a pointer variable
// 	var ptr *int
	  
// 	fmt.Println("Value of pointer:", ptr)
  
//   }

// func main(){
// 	var num int
// 	var ptr *int

// 	num = 11
// 	ptr = &num 

// 	fmt.Println(num, ptr)

// 	num = 22
// 	fmt.Println(num, ptr)

// 	fmt.Println(*ptr)

// 	*ptr = 10
// 	fmt.Println(num, ptr)

// }

// Program to pass pointer as a function argument


// func update(num *int) {

//   // dereferencing the pointer
//   *num = 30

// } 

// func main() {
 
//   var number = 55
//   fmt.Println(number) 

//   // function call
//   update(&number)
  
//   fmt.Println("The number is", number)

// }

// func main(){
// 	result := display()
// 	fmt.Println(*result)
// }

// func display() *string{
// 	message := "Hello World"
// 	return &message 
// }

// func callByValue(num int){
// 	num = 30 
// }

// func callByReference(num *int){
// 	*num = 10 
// }

// func main(){
// 	num := 20
// 	fmt.Println(num)

// 	callByValue(num)
// 	fmt.Println(num)

// 	callByReference(&num)
// 	fmt.Println(num) 
// }


// func main(){

// 	type Person struct{
// 	name string 
// 	id int
// 	}

// 	person1 := Person{
// 		name : "Abhishek",
// 		id : 1011,
// 	}

// 	var ptr *Person
// 	ptr = &person1 

// 	fmt.Println(person1)

// 	fmt.Println(ptr) 

// 	fmt.Println(ptr.name, ptr.id)

// 	ptr.id = 1122
// 	fmt.Println(person1.name, person1.id)

// }







