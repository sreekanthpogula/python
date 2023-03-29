a = range(5)
print(list(a))


def infinite_sequence():
    num = 0 
    while True:
        yield num
        num += 1
    for i in infinite_sequence():
        print(i, end=" ")
gen = infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def multiple_yield():
    value = "I'm here for the first time"
    yield value
    value = "My Second time here"
    yield value

multi_gen = multiple_yield()
print(next(multi_gen))