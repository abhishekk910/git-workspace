package main 

import "fmt"

func linearSearch(array []int, value int) int {
	for _, i := range array{
		if i == value{
			return i 
		}
	}
	return -1 
}

func main(){
	array := []int{95,78,46,58,45,86,99,251,320}
	fmt.Println(linearSearch(array, 58))
	fmt.Println(linearSearch(array, 101)) 
}

