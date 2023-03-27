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



