def binary_search(array, element):
    low = 0 
    high = len(array)-1 
    while low <= high:
        mid = (low + high)// 2
        if element == array[mid]:
            return mid 
        elif (element > array[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return -1 

array = [1 , 4, 8, 12, 15, 17, 19]
# element = 15 
element = 20
result = binary_search(array, element)
if result == -1:
    print("Element is not present in array.")
else:
    print(f"{element} is present at index {result}")


