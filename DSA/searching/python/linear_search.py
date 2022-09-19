def linear_search(array, search_element):
    global i 
    flag = False
    for i in range(len(array)):
        if array[i] == search_element:
            flag = True
            return flag 
    else:
        return flag 


# linear_search([12, 3, 45, 11, 8, 10], 45)
result = linear_search([12, 3, 45, 11, 8, 10], 101)
if result == True:
    print(f"Element is present at index {i}")
else:
    print(f"Element is not present in the array")
