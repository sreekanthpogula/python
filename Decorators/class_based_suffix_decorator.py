class SuffixDecorator:
    def __init__(self, suffix):
        self.suffix = suffix

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return self.suffix + result
        return wrapper
    
@SuffixDecorator('Sreekanth, ')
def my_func():
    return 'Hello!'

print(my_func())