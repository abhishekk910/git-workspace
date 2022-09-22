package main

import "fmt"

func binarySearch(array []int, element int)int{
	low := 0
	high := len(array) - 1
	for(low <= high){
		mid := (low + high) / 2
		if(element == array[mid]){
			return mid 
		}else if (element > array[mid]){
			low = mid + 1
		}else{
			high = mid - 1 
		}
	}
	return -1 
}

func main(){
	array := []int{1, 3, 5, 11, 15, 16, 19, 23}
	// element := 15
	element := 22
	result := binarySearch(array, element)
	if result == -1{
		fmt.Printf("%v is not present in %v", element, array)
	}else{
		fmt.Printf("%v is present in %v", element, array)
	}
}
