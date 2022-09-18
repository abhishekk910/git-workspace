def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i 
    return -1 

array = [15, 4, 32, 56, 11, 78, 43, 54, 87]
value = int(input("Enter the value to be searched in an array : "))
result = linear_search(array, value) 
if result == -1:
    print(f"Element {value} is not present in {array}")
else:
    print(f"Element {value} is present at index number {result}") 
