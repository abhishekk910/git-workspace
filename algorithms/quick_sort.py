def quick_sort(array):
    lesser = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                lesser.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)

        return quick_sort(lesser) + equal + quick_sort(greater)

    else:
        return array 

array = [ 10, 7, 8, 9, 1, 5]
print(array)
print(quick_sort(array))
