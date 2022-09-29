import numpy as np 

# creating 2d Array
twoD_array = np.array(
    [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
)

print(twoD_array)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]


# Adding a row to 2d array
newArray = np.insert(twoD_array, 0,[[10, 20, 30, 40]], axis=0)

# print(newArray)

# Adding a column to 2d array
newArray = np.insert(twoD_array, 1, [[10, 20, 30, 40]], axis=1)
print(newArray)


array_2d = [[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]]




