# In Python, decorators are a way to modify the behavior of functions or classes by wrapping them with another function. Decorators can accept arguments, which allows for more flexibility in their usage.

# To create a decorator that accepts arguments, you first define a function that takes the arguments you want to use. This function will then return another function, which will be the actual decorator. The decorator function takes the function or class you want to modify as an argument, and returns a new version of that function or class with the modifications you specified.

def repeat(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Sreekanth")


from functools import wraps

def repeat(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for _ in range(5):
            result = fn(*args, **kwargs)
        return result

    return wrapper


@repeat
def say(message):
    ''' print the message 
    Arguments
        message: the message to show
    '''
    print(message)


say('Hello')

class SuffixDecorator:
    def __init__(self, suffix):
        self.suffix = suffix

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return  result + self.suffix
        return wrapper
    
@SuffixDecorator(' !!!')
def my_function():
    return 'Hello World'

print(my_function())

class String_Concatination_Decorator:
    def __init__(self, addon_string):
        self.addon_string = addon_string

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return self.addon_string + result
        return wrapper
    
@String_Concatination_Decorator('Hello ')
def my_function():
    return 'Sreekanth'

print(my_function())

