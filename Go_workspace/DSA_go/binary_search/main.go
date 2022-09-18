package main

import "fmt"

func binarySearch(array []int, value int) int {
	low := 0
	high := len(array)-1 
	for low <= high{
		mid := low + (high-low)/ 2
		if array[mid] == value{
			return mid 
		}else if value > array[mid]{
			low = mid + 1
		}else{
			high = mid -1 
		}	 
	}
	return -1 
}

func main(){
	array := []int{1,2, 9, 20, 31, 45, 63, 70, 100}
	fmt.Println(binarySearch(array, 31))
	fmt.Println(binarySearch(array, 101)) 
}




