package main

import "fmt"

// // SimpleFunction prints a message
// func SimpleFunction() {
// 	fmt.Println("Hello World")
// }

// func add(x int, y int){
// 	total := 0
// 	total = x + y 
// 	fmt.Println(total)
// }

// func add(x int, y int)int{
// 	total := 0
// 	total = x + y
// 	return total 
// }

// func rectangle(length int, breadth int) (area int){
// 	area = length * breadth
// 	return
// }


// func rectangle(l int, b int) (area int, parameter int) {
// 	parameter = 2 * (l + b)
// 	area = l * b
// 	return area, parameter
// }

// var (
// 	area = func(l int, b int) int {
// 		return l * b
// 	}
// )

func main() {
	// SimpleFunction()
	// sum := add(10, 20) 
	// fmt.Println(sum) 
	// fmt.Println("Area : ", rectangle(10, 12))
	// var a, p int
	// a, p = rectangle(20, 30)
	// fmt.Println("Area:", a)
	// fmt.Println("Parameter:", p)

	// fmt.Println(area(20, 30))

	func(l int, b int) {
		fmt.Println(l * b)
	}(20, 30)
}


