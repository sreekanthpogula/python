# __new__: The __new__ method is used to create a new instance of a class.
class Singleton:
    instance = None
    
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 == singleton2) # Output: True
