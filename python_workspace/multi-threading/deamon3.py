from time import sleep
from threading import current_thread
from threading import Thread

def task():
    thread = current_thread()
    print(f'Daemon thread: {thread.daemon}')
    for i in range(1000):
        print(i)
        sleep(0.2)

thread = Thread(target=task, daemon=True)
thread.start()
sleep(3)
print('Main thread exiting...')

