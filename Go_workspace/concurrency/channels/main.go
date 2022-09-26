// package main

// import (  
//     "fmt"
// )

// func helloworld(c chan bool) {  
//     fmt.Println("Hello world goroutine")
//     c <- true
// }

// func main() {  
//     c := make(chan bool)
//     go helloworld(c)
//     d := <-c 
//     fmt.Println(d)
//     fmt.Println("main function")
// }

// package main 

// import "fmt"

// func calculateSquare(number int, square chan int) {
//     sum := 0
//     for number != 0{
//         digit := number % 10
//         sum += digit * digit
//         number = number / 10
//     }
//     square <- sum 
// }

// func calculateCube(number int, cube chan int) {
//     sum := 0
//     for number != 0{
//         digit := number % 10
//         sum += digit * digit * digit 
//         number = number / 10
//     }
//     cube <- sum 
// }

// func main(){
//     number := 123
//     square := make(chan int)
//     cube := make(chan int)
//     go calculateSquare(number, square)
//     go calculateCube(number, cube)
//     squares, cubes := <-square, <-cube
//     fmt.Println(squares + cubes)  
// }

// package main

// import "fmt"

// func sendData(sendch chan<- int) {  
//     sendch <- 10
// }

// func main() {  
//     channel := make(chan int)
//     go sendData(channel)
//     fmt.Println(<-channel)
// }

// package main

// import (  
//     "fmt"
// )

// func producer(chnl chan int) {  
//     for i := 0; i < 10; i++ {
//         chnl <- i
//     }
//     close(chnl)
// }

// func main() {  
//     ch := make(chan int)
//     go producer(ch)
//     for {
//         v, ok := <-ch
//         if ok == false {
//             break
//         }
//         fmt.Println("Received ", v, ok)
//     }
// }

// package main

// import (  
//     "fmt"
// )

// func producer(chnl chan int) {  
//     for i := 0; i < 10; i++ {
//         chnl <- i
//     }
//     close(chnl)
// }

// func main() {  
//     ch := make(chan int)
//     go producer(ch)
//     for v := range ch {
//         fmt.Println("Received ",v)
//     }
// }







