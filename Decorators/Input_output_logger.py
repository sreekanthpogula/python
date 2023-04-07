import functools

def log_input_output(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Input : args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)

        print(f"Output: {result}")
        return result
    return wrapper
@log_input_output
def multiply(x, y):
    return x * y

result = multiply(2, 3)
print(result)