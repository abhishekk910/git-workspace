# list1 = ['Python', 'Java', 'SQL', 'Golang']
# list2 = list1
# list3 = list1[:]
 
# list2[0] = 'C'
# list3[1] = 'C++'

# sum = 0
# for i in (list1, list2, list3):
#     print(i)
#     if i[0] == 'C':
#         sum += 1
#     if i[1] == 'C++':
#         sum += 20
# print(sum)

# arr = [[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14, 15]]
# for i in range(0, 4):
#     print(i)
#     print(arr[i]) 
#     print(arr[i].pop())
#     print() 
# print(arr) 

# def f(value, values):
#     v = 1
#     values[0] = 44
# t = 3
# v = [1, 2, 3]
# f(t, v)
# print(t, v[0])

# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# def fun(m):
#     v = m[0][0]
 
#     for row in m:
#         for element in row:
#             if v < element: v = element
 
#     return v
# print(fun(data[0]))

# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     arr[i - 1] = arr[i]
# for i in range(0, 6): 
#     print(arr[i], end = " ")

# def f(i, values = []):
#     values.append(i)
#     print (values)
#     return values
# f(1)
# f(2)
# f(3)

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# def findMissing(list, n):
#     sum1 = sum(list)
#     sum2 = 100*101/2
#     print(int(sum2-sum1))
# findMissing(mylist, 100)

list1 = [1,2,4]
list2 = [1,3,4]
res = []
# Output: [1,1,2,3,4,4]
for i in range(len(list1)):
    res.extend([list1[i], list2[i]])
print(res)



