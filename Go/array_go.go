package main
import "fmt"

// func main() {
//   var arrayOfInteger = [5]int{1, 5, 8, 0, 3}
//   fmt.Println(arrayOfInteger)
// }

// func main(){
// 	var strings = [3]string{"Python", "Java", "Hello World"}
// 	fmt.Println(strings)
// 	for i, v := range strings{
// 		fmt.Println(i, v)
// 	}
// }

// func main() {
// 	// declaring an array
// 	var arrayOfIntegers[3]int 
// 	// elements are assigned using index
// 	arrayOfIntegers[0] = 5
// 	arrayOfIntegers[1] = 10
// 	arrayOfIntegers[2] = 15
// 	fmt.Println(arrayOfIntegers)
// }

// func main() {
// 	// to initialize the elements of index 0 and 3 only
// 	arrayOfIntegers := [5]int{0: 7, 3: 9}
// 	fmt.Println(arrayOfIntegers)
// }

// func main() {
// 	arr := [3]string{"A", "B", "C"}
// 	// change the element of index 2
// 	arr[2] = "D"
// 	fmt.Println(arr)
// }

// func main(){
// 	// creating an array
// 	var arrayOfIntegers = [...]int{1, 5, 8, 0, 3, 10}
 
// 	// finding the length of array using len()
// 	length := len(arrayOfIntegers)
  
// 	fmt.Println("The length of array is", length)
// }

// func main() {
// 	array := [...]int{12, 4, 5, 10, 12}
// 	// loop through the array
// 	for i := 0; i < len(array); i++ {
// 	  fmt.Println(array[i])
// 	}
// }

func main() {
	// creating a 2 dimensional array
	arrayInteger := [2][2]int{{1, 2}, {3, 4}}
	// accessing the values of 2d array
	for i := 0; i < 2; i++ {
	  for j := 0; j < 2; j++ {
		fmt.Println(arrayInteger[i][j])
	  }
	}
}












