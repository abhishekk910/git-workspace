# from time import sleep, perf_counter

# def task(id):
#     print(f'Starting the task {id}...')
#     sleep(1)
#     return f'Completed with task {id}'

# start = perf_counter()

# print(task(1))
# print(task(2))

# finish = perf_counter()

# print(f"It took {finish-start} second(s) to finish.")


# from time import sleep, perf_counter
# from concurrent.futures import ThreadPoolExecutor

# def task(id):
#     print(f'Starting the task {id}...')
#     sleep(1)
#     return f'Completed with task {id}'

# start = perf_counter()

# with ThreadPoolExecutor() as executor:
#     f1 = executor.submit(task, 1)
#     f2 = executor.submit(task, 2)

#     print(f1.result())
#     print(f2.result())    

# finish = perf_counter()

# print(f"It took {finish-start} second(s) to finish.")

