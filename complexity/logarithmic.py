# 0(log n) - logarithmic time complexity

def reverse_number(number):
    temp = number
    reverse_number = 0
    while temp != 0:
        reminder = temp % 10
        reverse_number = reverse_number * 10 + reminder
        temp = temp // 10
    return number
print(reverse_number(145))
print(reverse_number(234)) 