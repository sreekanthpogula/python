# Main Concepts of Object-Oriented Programming (OOPs)
# Class
# Classes are created by keyword class.
# Attributes are the variables that belong to a class .
# Attributes are always public and can be accessed using the dot(.) operator.
# def class ClassName:
# statement-1
# statement-N
# def __init__(self):
# statement-1
# statement-2
# statement-3
# statement-4
# statement-5
# statement-6
# statement-7
# statement-8
from poetry.console.commands import self


# class Dog:
#     pass

# Objects
# The object is an entity that has a state and behavior associated with it
# obj = Dog()

# example

class Dog:
    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))


# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class methods
Rodger.speak()
Tommy.speak()


# Polymorphism simply means having many forms.
class Bird:
    def intro(self):
        print("I am a bird")

    def flight(self):
        print("most of the birds can fly")


class sparrow(Bird):
    def flight(self):
        print("sparrow can fly")


class Ostrich(Bird):
    def flight(self):
        print("ostrich cannot fly")


obj = Bird()
obj_sparrow = sparrow()
obj_ostrich = Ostrich()

obj.intro()
obj.flight()
obj_sparrow.intro()
obj_sparrow.flight()
obj_ostrich.intro()
obj_ostrich.flight()


# Encapsulation It describes the idea of wrapping data and the methods that work on data within one unit.


class Base:
    def __init__(self):
        self.a = "sreekanth"
        self.__b = "sreekanth"


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Derived")
        print(self.__b)


obj1 = Base()
print(obj1.a)


# Inheritance is the capability of one class to derive or inherit the properties from another class


class Person(object):
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def dispaly(self):
        print("".format(self.name))
        print("".format(self.id_number))

    def details(self):
        print("".format(self.name))
        print("".format(self.id_number))


class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, id_number)

    def details(self):
        print("Name is {}".format(self.name))
        print("ID number is {}".format(self.id_number))
        print("Salary is {}".format(self.salary))
        print("Post is {}".format(self.post))


a = Employee('rahul', 886012, 20000, "intern")
a.dispaly()
a.details()

# Data Abstraction It hides the unnecessary code details from the user.
from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self.discount = None

    def set_discount(self, discount):
        self.discount = discount

    def get_discount(self):
        self.discount = self.discount

    def get_price(self):
        if self.discount:
            return self.price * (1 - self.discount)
        else:
            return self.price

    @abstractmethod
    def __repr__(self):
        return f"Book: {self.title},Quantity: {self.quantity}, Author: {self.author},Price: {self.get_price()})"


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

    def __repr__(self):
        return f"Novel: {self.title},Quantity: {self.quantity},Author: {self.author},Price: {self.get_price()},Pages: {self.pages}"


novel1 = Novel('two states', 20, 'cheetan bhagat', 200, 187)
novel1.set_discount(0.20)
print(novel1)


# Method overloading It simply refers to the use of many methods with the same name that take various numbers of
# arguments within a single class.
class ParentClass:
    def call_me(self):
        print("Parent class")


class ChildClass:
    def call_me(self):
        print("Child class")


pobj = ParentClass()
pobj.call_me()

cobj = ChildClass()
cobj.call_me()


# method overloading
class ParentClass:
    def call_me(self):
        print("Parent class")

class ChildClass(ParentClass):
    def call_me(self):
        print("Child class")
pobj = ParentClass()
pobj.call_me()

cobj = ChildClass()
cobj.call_me()

