import threading

x = 0

def increment():
    global x 
    x += 1

def thread_task(lock):
    for _ in range(10000):
        lock.acquire()
        increment()
        lock.release()

def main_task():
    global x 
    x = 0

    # creating a lock
    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

for i in range(10):
    main_task()
    print(f"Iteration {i} : x = {x}")
