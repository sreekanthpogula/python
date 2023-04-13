# Factory Method is a creation design pattern that provides an interface for creating objects in a superclass,
# but allows subclasses to alter the type of objects that will be created.

# Usage examples: The Factory Method pattern is widely used in Python code. It’s very useful when you need to provide
# a high level of flexibility for your code.

# Identification: Factory methods can be recognized by creation methods that construct objects from concrete classes.
# While concrete classes are used during the object creation, the return type of the factory methods is usually
# declared as either an abstract class or an interface.


from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """ The creator class declares the factory method is supposed to return an object of a product class."""

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: the same creator's code has just worked {product.operation()}"
        return result


class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()
    
class ConcreteCreator3(Creator):
    def factory_method(Self) -> Product:
        return ConcreteProduct3()


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"

class ConcreteProduct3(Product):
    def operation(Self) -> str:
        return "{Result of the ConcreteProduct3}"

def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
    print("\n")
    print("App: Launched with the ConcreteCreator3.")
    client_code(ConcreteCreator3())
