# Dependency Injection is a software design pattern that allows the application components to depend on abstractions instead of concrete implementations. The goal of Dependency Injection is to decouple the components of an application, making them more reusable, testable, and maintainable. Decorators can be used to implement Dependency Injection in Python.

# Here's an example of how to use a decorator to implement Dependency Injection:

# Define a decorator that injects a dependency
def inject_dependency(dependency):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Inject the dependency into the function's arguments
            return func(dependency, *args, **kwargs)
        return wrapper
    return decorator

# Define a class that represents a dependency
class MyDependency:
    def some_method(self):
        return "Hello, Sreekanth!"

# Define a class that represents a service
@inject_dependency(MyDependency())
class MyService:
    def __init__(self, dependency):
        self.dependency = dependency
    
    def do_something(self):
        # Use the injected dependency
        result = self.dependency.some_method()
        print(result)

# Create an instance of the service and call the method
service = MyService()
service.do_something()
