import time


class CustomDecoratorContextManager:
    """ this is the CustomDecoratorContextManager class"""
    def __init__(self, filename=None):
        self.filename = filename

    def __enter__(self):
        if self.filename:
            self.file = open(self.filename, 'r')
            return self.file
        else:
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        if self.filename:
            self.file.close()

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(
                f"Function {func.__name__} was called at {time.ctime(start_time)}")
            print(
                f"Function {func.__name__} took {end_time - start_time:.2f} seconds to execute")
            return result
        return wrapper


# As a context manager
with CustomDecoratorContextManager('file.txt') as file:
    if file:
        content = file.read()
        print(content)


# As a decorator
@CustomDecoratorContextManager()
def my_function():
    """ this is a sample function"""
    time.sleep(2)
    print("Inside my_function")


my_function()
