import threading
import time 

x = 0
def thread_task(lock):
    global x 
    for i in range(10):
        time.sleep(1)
        x += 1

def main_task():

    lock = threading.Lock()
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))
    global start_time
    start_time = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    global end_time
    end_time = time.time()
    

if __name__ == "__main__":
    main_task()
    print(x) 
    print(end_time - start_time)
    

