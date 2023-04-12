# Multiprocessing is when multiple processes are spawn from the main process, each having its own CPU and memory.
import time
import multiprocessing


def some_task():
    for _ in range(100_000_000):
        x = 1 + 1
    print("Finished task")


if __name__ == "__main__":
    start = time.time()
    # Create two threads
    p1 = multiprocessing.Process(target=some_task)
    p2 = multiprocessing.Process(target=some_task)
    # Start running both threads
    p1.start()
    p2.start()
    # Wait until both threads are complete, and join the process into a single thread
    p1.join()
    p2.join()
    end = time.time()
    print(f"Finished process in {end - start} seconds")
