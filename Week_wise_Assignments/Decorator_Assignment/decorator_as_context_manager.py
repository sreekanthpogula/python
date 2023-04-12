from contextlib import ContextDecorator

class my_decorator(ContextDecorator):
    def __enter__(self):
        print('Entering the decorated function')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting the decorated function')

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return wrapper

@my_decorator()
def my_function():
    print('Inside the decorated function')

my_function()
