def selection_sort(array):
    for i in range(len(array)):
        min = i 
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j 
        array[i], array[min] = array[min], array[i] 
    return array

array = [20, 12, 10, 15, 2]
print(f"before sorting : {array}")
print(f"After Sorting : {selection_sort(array)}")


        