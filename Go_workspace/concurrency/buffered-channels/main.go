// package main

// import (  
//     "fmt"
// )

// func main() {  
//     ch := make(chan string, 2)
//     ch <- "Hello"
//     ch <- "World"
//     fmt.Println(<- ch)
//     fmt.Println(<- ch)
// }

// package main

// import (  
//     "fmt"
//     "time"
// )

// func write(ch chan int) {  
//     for i := 0; i < 5; i++ {
//         ch <- i
//         fmt.Println("successfully wrote", i, "to ch")
//     }
//     close(ch)
// }

// func main() {  
//     ch := make(chan int, 2)
//     go write(ch)
//     time.Sleep(2 * time.Second)
//     for v := range ch {
//         fmt.Println("read value", v,"from ch")
//         time.Sleep(2 * time.Second)
//     }
// }

// package main

// import (  
//     "fmt"
// )

// func main() {  
//     ch := make(chan string, 2)
//     ch <- "Python"
//     ch <- "Golang"
//     ch <- "Java"
//     fmt.Println(<-ch)
//     fmt.Println(<-ch)
// }


// closing buffered channels
package main

import (  
    "fmt"
)

// func main() {  
//     ch := make(chan int, 5)
//     ch <- 5
//     ch <- 6
//     close(ch)
//     n, open := <-ch 
//     fmt.Printf("Received: %d, open: %t\n", n, open)
//     n, open = <-ch 
//     fmt.Printf("Received: %d, open: %t\n", n, open)
//     n, open = <-ch 
//     fmt.Printf("Received: %d, open: %t\n", n, open)
// }

func main(){
	ch := make(chan string, 3)
	ch <- "Python"
	ch <- "Golang"
	fmt.Println("capacity is", cap(ch))
	fmt.Println("length is", len(ch))
	fmt.Println("read value", <-ch)
	fmt.Println("new length is", len(ch))
	fmt.Println("capacity is", cap(ch))
}





