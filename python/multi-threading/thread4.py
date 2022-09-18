import threading
import time 

def calculate_square(numbers):
    for number in numbers:
        time.sleep(1)
        print("Square:", number * number)

def calculate_cube(numbers):
    for number in numbers:
        time.sleep(1)
        print("Cube:", number * number * number)

numbers = list(range(1, 6))

initial_time = time.time()
thread1 = threading.Thread(target=calculate_square, args=(numbers, ))
thread2 = threading.Thread(target=calculate_cube, args=(numbers, ))


thread1.start()
thread2.start()

thread1.join()
thread2.join()

final_time = time.time()
print("Time Taken : ", final_time - initial_time)
