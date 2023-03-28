def addone(func):
    def wrapper(x):
        return func(x) + 1
    return wrapper

def subfour(func):
    def wrapper(x):
        return func(x) - 4
    return wrapper

@addone
def multiply(y):
    return y * 2

@subfour
def divide(a):
    return a / 10

print(multiply(2))
print(divide(100))
