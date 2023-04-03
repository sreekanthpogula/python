async def prime_generator():
    num = 2
    primes = []

    while True:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break

        if is_prime:
            Value = yield num 
            primes.append(num)
        else:
            pass

        num += 1

async def main():
    async for prime in prime_generator():
        print(prime)
        if prime > 20:
            break 
        await main()
