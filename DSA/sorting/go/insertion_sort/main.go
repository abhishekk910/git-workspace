package main

import "fmt"

func InsertionSort(array []int) []int {
	for i := 1; i < len(array); i++ {
		j := i
		for j > 0 {
			if array[j-1] > array[j] {
				array[j-1], array[j] = array[j], array[j-1]
			}
			j = j - 1
		}
	}
	return array 
}

func main() {
	array1 := []int{10, 12, 1, 13, 15}
	fmt.Println(array1)
	fmt.Println(InsertionSort(array1))

	array2 := []int{5, 4, 3, 2, 1}
	fmt.Println(array2)
	fmt.Println(InsertionSort(array2))
}
