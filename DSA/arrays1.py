"""
 Input: 
    arr = [10, 20, 30, 40, 50]
    Output:
    sum = 150
"""

# arr = [10, 20, 30, 40, 50]
# total = 0
# for i in (arr):
#     total += i
# print(total) 

# res = sum(arr)
# print(res) 

# Python program to find the occurrence of a particular number in an array

# def count_element(nums):
#     count = 0
#     for num in nums:
#         if num == 3:
#             count += 1
#     return count 
# print(count_element([1,2,3,4,3,3,3]))

# Python program to find the Largest element of the array 

# function to find the Largest element of array
# def FindLargestElement(arr,n):
# 	maxVal = arr[0]
# 	for i in range(1, n):
# 		if arr[i] > maxVal:
# 			maxVal = arr[i]
# 	return maxVal
# n = int(input("Enter the number of elements in the array: "))
# arr = []
# print("Enter elements of the array: ")
# for i in range(n):
#   numbers = int(input())
#   arr.append(numbers)
# maxVal = FindLargestElement(arr,n)
# print ("Largest in given array is",maxVal)

"""
#  Python program to find the remainder of array multiplication by divisor 
def arrayMultiplication(array, n, D):
    product = 1
    for i in range(n):
        product = product * i
    return (product % D) 
n = int(input("Enter number of elements of the array: "))
arr = []
print("Enter elements of the array:")
for i in range(n):
    numbers = int(input())
    arr.append(numbers)
D = int(input("Enter divisor: "))
rem = arrayMultiplication(arr, n, D)
print("The remainder of array multiplication by divisor is ", rem)
"""

"""
matrix = [[10,20,30], [40,50,60],[70,80,90]]
print(matrix) 

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print() 
"""

matrix1 = ()
row = int(input("Enter Row : "))
col = int(input("Enter Columns : "))
print("Matrix 1 : ")
for i in range(row):
    c=()
    for j in range(col):
      v=int(input("Enter Value {},{}:".format(i,j)))
      c+=(v,)
    matrix1 += (c,)

matrix2 = ()
print("Matrix 2 : ")
for i in range(row):
    c = ()
    for j in range(col):
        v = int(input("Enter Value {},{}:".format(i, j)))
        c += (v,)
    matrix2 += (c,)

print("Value of matrix 1 : ", end = " ")
print(matrix1)
print("Value of matrix 2 : ", end = " ")
print(matrix2)

sum_matrix = ()
print("Sum Matrix : ", end = " ")
for i in range(row):
    c=()
    for j in range(col):
        v = matrix1[i][j] + matrix2[i][j]
        c += (v,)
    sum_matrix += (c,)
print(sum_matrix) 






