def binary_search(array, value):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = low + (high-low)//2
        if array[mid] == value:
            return mid 
        elif value > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1 

array = [23, 11, 56, 77, 8, 2, 98, 34]
array.sort() 
print(array) 
value = int(input("Enter the value to be searched in an array : "))

result = binary_search(array, value)
if result == -1:
    print(f"Element {value} is not present in {array}")
else:
    print(f"Element {value} is present at index number {result}") 



