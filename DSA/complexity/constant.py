# 0(1) - Constant Time complexity

def constant_algo(elements):
    result = elements[0] * elements[0]
    print()
constant_algo([4,5,6,7])


def first_and_last_of_list(list):
    print("first element : ", list[0])
    print("last element : ", list[-1])
    print("=========")

first_and_last_of_list([0])
first_and_last_of_list([1,2,3,4])
first_and_last_of_list([i for i in range(1000)])
first_and_last_of_list([i for i in range(10000)])



