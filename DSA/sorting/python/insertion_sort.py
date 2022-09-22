def insertion_sort(array):
    for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j+1] = array[j]
                j = j - 1
            array[j+1] = key

if __name__ == "__main__":
    array = [10, 3, 1, 2, 4]
    array = [5, 15, 10, 3, 1]
    print(array)
    insertion_sort(array)
    print(array)
