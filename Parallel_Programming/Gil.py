# GIL stands for Global Interpreter Lock, and it is a mechanism used in the CPython implementation of Python to ensure that only one thread can execute Python bytecode at a time. This can limit the performance of multithreaded programs in Python, since multiple threads cannot execute Python code concurrently. However, the GIL does not prevent concurrent execution of I/O-bound tasks or tasks that use external libraries that release the GIL, such as NumPy or Pandas.

import threading

def worker():
    while True:
        print("I'm from the worker")

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

# wait for all threads to finish
for t in threads:
    t.join()
    t.sleep()

