// package main

// import (
// 	"fmt"
// )

// func hello() {
// 	fmt.Println("Hello world goroutine")
// }

// func main() {
// 	go hello()
// 	fmt.Println("main function")
// }

// package main

// import (  
//     "fmt"
//     "time"
// )

// func hello() {  
//     fmt.Println("Hello world goroutine")
// }
// func main() {  
//     go hello()
//     time.Sleep(1 * time.Second)
//     fmt.Println("main function")
// }

package main

import (
	"fmt"
	"time"
)


func numbers(){
	for i:=1; i <= 5; i++{
		time.Sleep(3 * time.Second)
		fmt.Printf("%d ", i)
	}
}

func alphabets(){
	for i:= 'a'; i <= 'e'; i++{
		time.Sleep(2* time.Second)
		fmt.Printf("%c ", i)
	}
}

func main(){
	go numbers()
	go alphabets()
	time.Sleep(20 * time.Second)
	fmt.Println("Main Goroutine Completed..!")
}


