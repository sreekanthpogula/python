# __slots__: The __slots__ attribute is used to limit the attributes of a class.
class Person:
    __slots__ = ('name', 'age')

person = Person()
person.name = 'John'
person.age = 30
person.gender = 'Male'