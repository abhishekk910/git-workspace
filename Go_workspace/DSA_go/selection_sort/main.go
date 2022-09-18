package main

import (
	"fmt"
)

func selectionSort(array []int) []int{
	for i := 0; i < len(array); i++{
		min_index := i 
		for j := i+1; j < len(array); j++{
			if array[j] < array[min_index]{
				min_index = j 
			}
		}
		temp := array[i]
		array[i] = array[min_index]
      	array[min_index] = temp
	}
	return array 
}

func main(){
	array := []int{2,4,3,1,6,8,5}
	fmt.Println(array)
	fmt.Println(selectionSort(array))
}

