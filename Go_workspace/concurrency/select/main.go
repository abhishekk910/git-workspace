// package main

// import (
// 	"fmt"
// 	"time"
// )

// func function1(ch chan string){
// 	time.Sleep(4 * time.Second)
// 	ch <- "from function1"
// }

// func function2(ch chan string){
// 	time.Sleep(6 * time.Second)
// 	ch <- "from function2"
// }

// func main(){
// 	channel1 := make(chan string)
// 	channel2 := make(chan string)
// 	go function1(channel1)
// 	go function2(channel2)
// 	select{
// 	case s1 := <-channel1:
// 		fmt.Println(s1)
// 	case s2 := <-channel2:
// 		fmt.Println(s2)
// 	}
// }

// package main

// import (
// 	"fmt"
// 	"time"
// )

// func testing(ch chan string){
// 	time.Sleep(11 * time.Second)
// 	ch <- "testing completed.."
// }

// func main(){
// 	channel := make(chan string)
// 	go testing(channel)
// 	for{
// 		time.Sleep(1 * time.Second)
// 		select{
// 		case value := <- channel:
// 			fmt.Println("received :", value)
// 			return 
// 		default:
// 			fmt.Println("no value received..")
// 		}
// 	}
// }

// package main

// import "fmt"

// func main() {  
//     channel := make(chan string)
//     select {
//     case <-channel:
//     default:
//         fmt.Println("default case executed")
//     }
// }

// package main

// import "fmt"

// func main() {  
//     var channel chan string
//     select {
//     case v := <-channel:
//         fmt.Println("received value", v)
//     default:
//         fmt.Println("default case executed")

//     }
// }

package main

import (
	"fmt"
	"time"
)

func function1(ch chan string){
	ch <- "from function1"
}

func function2(ch chan string){
	ch <- "from function2"
}

func main(){
	channel1 := make(chan string)
    channel2 := make(chan string)
	go function1(channel1)
	go function2(channel2)
	time.Sleep(2 * time.Second)
	select{
	case s1 := <- channel1:
		fmt.Println(s1)
	case s2 := <- channel2:
		fmt.Println(s2) 
	}
}







