import numpy as np 

array_2d = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]]) 

print(array_2d)

def fetch_element(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])

fetch_element(array_2d, 2, 2)

