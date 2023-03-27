def add_one(func):
    def wrapper(x):
        return func(x) + 1
    return wrapper

def subtract_one(func):
    def wrapper(x):
        return func(x) - 1
    return wrapper

@add_one
def foo(x):
    return x * 2

@subtract_one
def bar(x):
    return x * 3

print(foo(3)) # output: 7
print(bar(4)) # output: 11
