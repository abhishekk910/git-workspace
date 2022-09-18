def bubble_sort(array):
    for i in range(len(array)-1,0,-1):
        swap = False
        for j in range(i):
            if array[j] > array[j+1]:
                swap = True 
                array[j], array[j+1] = array[j+1], array[j]
        if swap == False:
            return array
    return array 

array = [45, 89, 2, 145, 501, 78, 98, 76]
print(f"Before Sorting : {array}")
print(f"After Sorting :{bubble_sort(array)}")





