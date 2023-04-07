# Multithreading is the ability of an operating system or a program to manage multiple threads simultaneously, allowing different parts of a program to execute independently and concurrently. This can improve performance and responsiveness in applications that need to perform multiple tasks at the same time. For example, a web server may use multiple threads to handle incoming requests, so that one thread can handle one request while another thread is waiting for the next request.
import threading

def worker():
    print("Worker started")
    # Do Something
    print("Worker finished")
    
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
    
# wait for all the threads to finish
for t in threads:
    t.join()
