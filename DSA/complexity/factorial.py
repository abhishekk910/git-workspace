# 0(n!) Factorial Time

def factorial_number(number):
    if number == 1:
        return number
    else:
        return number * factorial_number(number-1)

print(factorial_number(5))
print(factorial_number(10))
print(factorial_number(100))

