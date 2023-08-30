def count_calls(func):
    count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function {func.__name__} has been called {count} times.")
        return func(*args, **kwargs)
    
    return wrapper

@count_calls
def say_hello():
    print("Hello!")

say_hello()
say_hello()
