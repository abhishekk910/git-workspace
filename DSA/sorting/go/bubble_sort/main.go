package main

import (
	"fmt"
)

func BubbleSort(array[] int) []int{
	for i := 0; i < len(array)-1; i++{
		for j := 0; j < len(array)-i-1; j++{
			if (array[j] > array[j+1]){
				array[j], array[j+1] = array[j+1], array[j]
			}
		}
	}
	// fmt.Println(array)
	return array 
}

func main(){
	// array := []int{12, 1, 3, 4, 2}
	array1 := []int{1, 3, 4, 2, 12}
	fmt.Println(array1)
	fmt.Println(BubbleSort(array1))
	array2 := []int{11, 7, 13, 4, 6}
	fmt.Println(array2)
	fmt.Println(BubbleSort(array2))
}
