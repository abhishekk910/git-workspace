# 0(n^2) - Quadratic Time

def add_2D_list_elements(list):
    sum = 0
    for i in list:
        for j in i:
            sum += j 
    print(sum) 
add_2D_list_elements([[1,2], [3,4]])
add_2D_list_elements([[1,2,3], [4,5,6], [7,8,9]])


