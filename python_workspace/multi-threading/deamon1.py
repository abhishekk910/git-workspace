# from threading import current_thread
# # get the current thread
# thread = current_thread()
# # report if daemon thread
# print(f'Daemon thread: {thread.daemon}')


from threading import current_thread, Thread 
from time import sleep 

# def task():
#     thread = current_thread()
#     print(f'Daemon thread: {thread.daemon}')

# thread = Thread(target=task)
# thread.start()

# def task():
#     thread = current_thread()
#     print(f'Daemon thread: {thread.daemon}')

# thread = Thread(target=task, daemon=True)
# thread.start()
# sleep(1) 


def task():
    thread = current_thread()
    print(f'Daemon thread: {thread.daemon}')

thread = Thread(target=task, daemon=True)
thread.daemon = True
thread.start()
sleep(1) 

