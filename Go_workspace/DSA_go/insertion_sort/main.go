package main

import "fmt"

func insertionSort(array []int) []int {
	for i := 1; i < len(array); i++ {
		key := array[i]
		j := i - 1
		for j >= 0 && array[j] > key {
			array[j+1] = array[j]
			j--
		}
		array[j+1] = key
	}
	return array
}

func main() {
	array := []int{13, 2, 78, 65, 4}
	fmt.Println(array)
	fmt.Println(insertionSort(array))
}

