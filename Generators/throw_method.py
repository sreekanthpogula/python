from generator_methods import getPrimes


prime_gen = getPrimes()

for x in prime_gen:
    if x > 10:
        prime_gen.throw(ValueError, "I think it was enough!")
    print(x)