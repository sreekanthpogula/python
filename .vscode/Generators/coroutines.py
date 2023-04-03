# Generator vs coroutine
# Generator example
def my_generator():
    for i in range(3):
        yield i

gen = my_generator()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

# Coroutine example
def my_coroutine():
    while True:
        x = yield
        print('Received:', x)

coro = my_coroutine()
next(coro)          # Prime the coroutine
coro.send('Hello')  # Received: Hello
coro.send('World')  # Received: World
