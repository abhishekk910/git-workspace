import numpy as np 

array_2d = np.array([[1,2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) 

print(array_2d)

# def traverse_array(array):
#     counter = 1
#     for i in range(len(array)):
#         print(f"row {counter} elements")
#         for j in range(len(array[0])):
#             print(array[i][j])
#         counter += 1 

# traverse_array(array_2d)

# def search_element(array, element):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             if array[i][j] == element:
#                 return f"Element {element} present at index {i} {j}"
#     else:
#         return f"Element {element} is not present in an array"
# print(search_element(array_2d, 11))

new_array = np.delete(array_2d, 2, axis=1)
print(new_array)




