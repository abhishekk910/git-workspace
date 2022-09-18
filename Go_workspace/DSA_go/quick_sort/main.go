package main

import "fmt"

func quickSort(array []int, low, high int) {
	if low < high {
		var pivot = partition(array, low, high)
		quickSort(array, low, pivot)
		quickSort(array, pivot+1, high)
	}
}

func partition(array []int, low, high int) int {
	var pivot = array[low]
	var i = low
	var j = high
	for i < j {
		for array[i] <= pivot && i < high {
			i++
		}
		for array[j] > pivot && j > low {
			j--
		}

		if i < j {
			var temp = array[i]
			array[i] = array[j]
			array[j] = temp
		}
	}
	array[low] = array[j]
	array[j] = pivot
	return j
}

func main() {
	var array = []int{15, 3, 12, 6, -9, 9, 0}
	fmt.Println(array)
	quickSort(array, 0, len(array)-1)
	fmt.Println(array)
}


