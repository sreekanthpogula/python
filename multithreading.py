# Multithreading means having the same process run multiple threads concurrently, sharing the same CPU and memory.

import time
import threading


def some_task():
    time.sleep(1)
    print("Finished task")


if __name__ == "__main__":
    start = time.time()
    # Create two threads
    t1 = threading.Thread(target=some_task)
    t2 = threading.Thread(target=some_task)
    # Start running both threads
    t1.start()
    t2.start()
    # Wait until both threads are complete, and join the process into a single thread
    t1.join()
    t2.join()
    end = time.time()
    print(f"Finished process in {end - start} seconds")
