# __str__: The __str__ method is used to provide a string representation of an object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}, {self.age}"

person = Person('John', 30)
print(person) # Output: John, 30
