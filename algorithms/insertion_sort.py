def insertion_sort(array):
    for i in range(1, len(array)):
        j = i-1
        temp = array[i] 
        while j >= 0 and temp < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = temp 
    return array 

array = [12, 11, 13, 5, 6]
print(array)
print(insertion_sort(array))


