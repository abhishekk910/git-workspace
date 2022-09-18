package main
import "fmt"

func main() {
  // declaring slice variable of type integer
  // numbers := []int{1, 2, 3, 4, 5}
  // // print the slice
  // fmt.Println("Numbers: ", numbers)

  // numbers := [8]int{10, 20, 30, 40, 50, 60, 70, 80}
  // sliceNumbers := numbers[4 : 7]
  // fmt.Println(sliceNumbers)

  // primeNumbers := []int{2, 3}
  // // add elements 5, 7 to the slice
  // primeNumbers = append(primeNumbers, 5, 7)
  // fmt.Println("Prime Numbers:", primeNumbers)

  // evenNumbers := []int{2, 4}
  // oddNumbers := []int{1, 3} 
  // evenNumbers = append(evenNumbers, oddNumbers...)
  // fmt.Println("Numbers:", evenNumbers)

  // create two slices
  // primeNumbers := []int{2, 3, 5, 7}
  // numbers := []int{1, 2, 3}
  // // copy elements of primeNumbers to numbers
  // copy(numbers, primeNumbers)
  // // print numbers
  // fmt.Println("Numbers:", numbers)


  // numbers := []int{1, 5, 8, 0, 3}
  // length := len(numbers)
  // fmt.Println("Length:", length)

  // numbers := []int{2, 4, 6, 8, 10}
  // // for loop that iterates through the slice
  // for i := 0; i < len(numbers); i++ {
  // fmt.Println(numbers[i])
  // }

  numbers := make([]int, 5, 7)
    // add elements to numbers
  numbers[0] = 13
  numbers[1] = 23
  numbers[2] = 33
  fmt.Println("Numbers:", numbers)
    

}

