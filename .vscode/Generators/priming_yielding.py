def my_coroutine():
    x = yield
    print('Received:', x)
    y = yield 2
    print('Received:', y)


coro = my_coroutine()
next(coro)
coro.send('Hello')
result = coro.send('World')
print(result)