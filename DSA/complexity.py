# def search(array, e):
#     for i,v in enumerate(array):
#         if v == e:
#             return i 
#     return -1 

# array = [12, 1, 34, 11]
# e = 1
# print(f"x is present at index {search(array, e)} ")


def get_num(array, num):
    if num%2 == 0:
        return 0
    sum = 0
    for i in range(num):
        sum += array[i]
    return sum 

array1 = [1,2,3,4]
n1 = len(array1)
print(get_num(array1, n1))

array2 = [2, 3, 12, 45, 3]
n2 = len(array2)
print(get_num(array2, n2)) 
