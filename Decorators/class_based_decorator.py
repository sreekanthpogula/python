# A class-based decorator is a decorator that is implemented as a Python class. It works in the same way as a regular function-based decorator but allows for more advanced functionality by using the object-oriented features of Python.

# To create a class-based decorator, you define a class with a __call__() method that takes a function as its argument. This method is called whenever the decorated function is called, allowing you to modify its behavior.

# Here is an example of a class-based decorator that adds a prefix to the result of a function:

class PrefixDecorator:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return self.prefix + result
        return wrapper
    
@PrefixDecorator('Result: ')
def my_function():
    return 'Hello World'

print(my_function())