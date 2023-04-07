# yield returns from a simple generator function, yield from allows you to yield from another generator function. This comes in handy when you need to use two functions in a generator such as when we did merge sort in the sorting 
def yieldOnly():
    yield "A"
    yield "B"
    yield "C"

def yieldFrom():
    for i in [1, 2, 3]:
        yield from yieldOnly()

test = yieldFrom()
for i in test:
    print(i)


# Sample program for yield from
def sample_generator(i):
    for j in range(i):
        yield j

def yf_generator(i):
    yield from sample_generator(i)
for value in yf_generator(5):
    print(value)
