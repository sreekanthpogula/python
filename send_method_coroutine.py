# import asyncio

# async def my_coroutine():
#     print('Coroutine started')
#     value = await asyncio.sleep(1)
#     print(f'Coroutine received value: {value}')
#     result = await asyncio.sleep(1)
#     print(f'Coroutine received result: {result}')

# async def main():
#     coro = my_coroutine()
#     print('Main coroutine started')
#     await asyncio.sleep(0.5)
#     print('Main coroutine sending value to my_coroutine')
#     await coro  # This will start the coroutine and reach the first yield statement
#     try:
#         coro.send('Hello')
#     except StopIteration:
#         pass
#     await asyncio.sleep(0.5)
#     print('Main coroutine sending result to my_coroutine')
#     try:
#         coro.send(42)
#     except StopIteration:
#         pass

# asyncio.run(main())

# Sample program
def isPrime(n):
    if n < 2 or n % 1 > 0:
        return False
    elif n == 2 or n == 3:
        return True
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

def getPrimes():
    value = 0
    while True:
        if isPrime(value):
            i = yield value
            if i is not None:
                value = i
        value += 1

prime_gen = getPrimes()
print(next(prime_gen))
print(prime_gen.send(1000))
print(next(prime_gen))  