list1 = []

def push(list1,element):
    list1.insert(0, element)

def pop(list1):
    list1.pop(-1)

def insert(list1,element, index):
    list1.insert(index, element)

push(list1, 10)
push(list1, 20)
print(list1)
insert(list1, 30, 1)
print(list1)
pop(list1)
print(list1)