import time 

def calculate_square(numbers):
    for number in numbers:
        time.sleep(1)
        print(number * number)

def calculate_cube(numbers):
    for number in numbers:
        time.sleep(1)
        print(number * number)


numbers = list(range(1, 6))
initial_time = time.time()
calculate_square(numbers)
calculate_cube(numbers)

final_time = time.time()
print("time taken :", final_time - initial_time)

