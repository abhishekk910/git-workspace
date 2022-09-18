package main

import "fmt"

func main() {
	// variadicExample("red", "blue", "green", "yellow")

	// variadicExample()
	// variadicExample("red", "blue")
	// variadicExample("red", "blue", "green")
	// variadicExample("red", "blue", "green", "yellow")

	fmt.Println(calculation("Rectangle", 20, 30))
	fmt.Println(calculation("Square", 20))
}

// func variadicExample(s ...string) {
// 	fmt.Println(s[0])
// 	fmt.Println(s[3])
// }

// func variadicExample(s ...string) {
// 	fmt.Println(s)
// }

func calculation(str string, y ...int) int {
	area := 1
	for _, val := range y {
		if str == "Rectangle" {
			area *= val
		} else if str == "Square" {
			area = val * val
		}
	}
	return area

}
