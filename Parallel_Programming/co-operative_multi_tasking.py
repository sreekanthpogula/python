# Cooperative multitasking is a technique used in asynchronous programming to allow multiple tasks to run concurrently without using multiple threads or processes. Each task must yield control periodically to allow other tasks to run, rather than relying on preemption by the operating system. This can be more efficient than using multiple threads or processes, since there is less overhead and no need for context switching. For example, an event loop in an asyncio program may use cooperative multitasking to run multiple coroutines concurrently, without blocking on I/O-bound tasks.


import asyncio

async def task1():
    while True:
        print("Task 1")
        await asyncio.sleep(1)

async def task2():
    while True:
        print("Task 2")
        await asyncio.sleep(2)

async def main():
    # create an event loop
    loop = asyncio.get_event_loop()

    # add the coroutines to the event loop
    loop.create_task(task1())
    loop.create_task(task2())

    # run the event loop indefinitely
    await asyncio.sleep(3600)

# start the program
asyncio.run(main())

