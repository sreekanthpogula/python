# .send method 
import asyncio


def isPrime(n):
    if n < 2 or n % 1 > 0:
        return False
    elif n == 2 or n == 3:
        return True
    for x in range(2, int(n**0.5) + 1):
        if n  % x == 0 :
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

