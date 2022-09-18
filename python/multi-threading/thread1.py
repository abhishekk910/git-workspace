import threading

def print_cube(num):
    print(f"Cube : {num * num * num}")

def print_square(num):
    print(f"Square : {num * num}")

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_cube, args=(10,))
    t2 = threading.Thread(target=print_square, args=(10,))

    # start thread 1
    t1.start()
    # start thread 2
    t2.start()

    # wait until thread 1 is completely executed.
    t1.join()

    # wait until thread 1 is completely executed.
    t2.join()

    print('completed..!')
