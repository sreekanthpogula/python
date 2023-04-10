class DependencyInjector:
    def __init__(self):
        self.dependencies = {}

    def register_dependency(self, name, dependency):
        self.dependencies[name] = dependency

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for name, dependency in self.dependencies.items():
                kwargs[name] = dependency
            return func(*args, **kwargs)
        return wrapper

dependency_injector = DependencyInjector()

class MyDependency:
    def __init__(self):
        self.value = 42

dependency_injector.register_dependency('my_dependency', MyDependency())

@dependency_injector
def my_function(my_dependency):
    print(my_dependency.value)

my_function()
