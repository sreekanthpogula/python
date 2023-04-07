# Locking is a technique used in multithreaded programming to synchronize access to shared resources, such as variables or files. When multiple threads need to access a shared resource, they may interfere with each other and cause race conditions or other errors. Locking provides a way to ensure that only one thread can access the resource at a time, preventing these errors. For example, a program that updates a shared counter variable may use a lock to ensure that only one thread can update the counter at a time.

import threading

counter = 0
lock = threading.Lock()

def worker():
    global counter
    with lock:
        counter += 1

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

# wait for all threads to finish
for t in threads:
    t.join()

print(counter)
