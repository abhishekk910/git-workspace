# 0(2^n) exponential time

def fibonacci_number(number):
    if number <= 1:
        return number 
    return fibonacci_number(number-1) + fibonacci_number(number-2)

for i in range(1, 10):
    print(fibonacci_number(i)) 
