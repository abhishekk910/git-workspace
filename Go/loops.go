package main
import ("fmt")

// func main() {
//   for i:=0; i < 5; i++ {
//     fmt.Println(i)
//   }
// }

// func main() {
// 	for i:=10; i <= 100; i+=10 {
// 	  fmt.Println(i)
// 	}
// } 

// func main() {
// 	for i:=0; i < 5; i++ {
// 	  if i == 3 {
// 		continue
// 	  }
// 	 fmt.Println(i)
// 	}
// }

func main() {
	for i:=0; i < 5; i++ {
	  if i == 3 {
		break
	  }
	 fmt.Println(i)
	}
} 

