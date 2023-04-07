def spanish(func):
    def wrapper():
        return "<spanish>" + func() + "<spanish>"
    return wrapper

def german(func):
    def wrapper():
        return "<german>" + func() + "<german>"
    return wrapper

@spanish
@german
def greet():
    return "Hello, Good Afternoon!"

print(greet())