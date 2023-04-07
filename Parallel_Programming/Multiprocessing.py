# Multiprocessing is a technique used to execute multiple processes simultaneously on a computer with multiple processors or cores. Each process runs in its own memory space and can execute independently, allowing for true parallelism. This can improve performance for CPU-bound tasks that can be split into smaller subtasks that can be executed in parallel. For example, a program that performs intensive calculations on large datasets may use multiprocessing to split the data into chunks and execute the calculations on multiple cores.

import multiprocessing

def worker(data):
    # do some work here
    return data

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    with multiprocessing.Pool() as pool:
        results = pool.map(worker, data)
        print(results)
