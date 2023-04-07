# Descriptors in Python are objects that define how attribute access works for an instance of a class. Decorators, on the other hand, are functions that take another function as input and extend or modify its behavior. In Python, it is possible to use descriptors as decorators to modify the behavior of a class attribute.

# To use a descriptor as a decorator, we can define the descriptor object, and then apply it to a class attribute using the @ syntax. For example, let's say we have a descriptor called UpperCase, which ensures that a string attribute is always in upper case. Here's how we can use it as a decorator:

class PositiveNumber:
    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be positive")
        instance._value = value

class MyClass:
    def __init__(self, value):
        self._value  = value

    my_number = PositiveNumber()

my_instance = MyClass(5)
print(my_instance.my_number)
try:
    my_instance.my_number = 5 # should raise a ValueError
except ValueError as e:
    print(e)
