# def bubble_sort(array):
#     for i in range(len(array)-1, 0, -1):
#         swap = False
#         for j in range(i):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#                 swap = True
#         if swap == False:
#             return array 
#     return array
# array = [13, 1, 78, 67, 34]
# print(array) 
# print(bubble_sort(array))


# def selection_sort(array):
#     for i in range(len(array)):
#         min = i 
#         for j in range(i+1, len(array)):
#             if array[min] > array[j]:
#                 min = j 
#         array[i], array[min] = array[min], array[i] 
#     return array

# array = [64, 25, 12, 22, 11]
# print(array) 
# print(selection_sort(array))

def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:]) 
print(list_sum([2, 4, 5, 6, 7]))

def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element
	return total
print(recursive_list_sum([1, 2, [3,4],[5,6]]))
print(recursive_list_sum([[1,2],[3,4]]))

def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(5))

def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * (factorial(n - 1))
print(factorial(5))

def sum_of_digits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sum_of_digits(int(n / 10))
print(sum_of_digits(234))
print(sum_of_digits(15))

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter range:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))

