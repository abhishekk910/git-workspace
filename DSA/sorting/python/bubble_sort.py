def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        swap = False
        for j in range(0, i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap = True
        if swap == False:
            break 
        

if __name__ == "__main__":
    array = [5, 1, 4, 2, 8]
    print(array)
    array = [1, 2, 1, 4, 5]
    print(array)
    bubble_sort(array)
    print(array)

