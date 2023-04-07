# Property decorator: The @property decorator in Python is used to define a method as a read-only property. It is a built-in decorator that is used to access a method like an attribute.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width
    
rect = Rectangle(5, 6)
print(rect.area)




























