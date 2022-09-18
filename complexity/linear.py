# 0(n) - Linear Time Complexity

def add_list_elements(list):
    sum = 0
    for i in list:
        sum += i 
    print("sum of all elements of list is : ", sum)
    print("========")

add_list_elements([0])
add_list_elements([1,2,3,4])
add_list_elements([i for i in range(1000)])
add_list_elements([i for i in range(100000)])

def linear(list):
    for i in list:
        print(i)
linear([4, 5, 6, 7])


