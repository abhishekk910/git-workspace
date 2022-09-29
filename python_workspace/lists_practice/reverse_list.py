def reverse_list(list1):
    list2 = []
    for i in range(len(list1)-1,-1,-1):
        list2.append(list1[i])
    return list2
list1 = [1,2,3,4,5]
print(reverse_list(list1))