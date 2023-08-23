# Introduction to Python

# Topic 1: Overview of Python and its applications
# Python is a versatile, high-level programming language known for its readability and ease of use. It's used in web development, data analysis, machine learning, and more.

# Topic 2: Setting up Python environment
# To start coding in Python, we need to install Python itself and a code editor. downloaded Python specific version from python.org and choose a code editor like Visual Studio Code or PyCharm.

# Topic 3: Writing and running a basic Python program (Hello World)
print("Hello, World!")
print("hello I'm Sreekanth")

# Topic 4: Understanding variables and data types
# Variables are containers for storing data. Common data types include integers (int), floating-point numbers (float), and strings (str).

x = "Hello, world!"  # string representation
y = 20  # integer representation
a = 20.5  # float representation
real_number = 1 + 29j  # complex number representation
fruits = ["apple", "orange", "banana"]  # list representation
vegetables = ("tomato", "carrot", "cabbage")  # tuple representation
distance = range(5)  # range representation
dict1 = {"a": 1, "b": 2, "c": 3}  # dictionary representation
team = {"apple", "banana", "cherry"}  # set representation
bread = frozenset({"apple", "banana", "cherry"})  # frozenset representation
b = True  # boolean representation
z = b"Hello"  # byte representation
c = bytearray(5)  # bytearray representation
m = memoryview(bytes(5))  # memory view representation
d = None  # None representation

# Topic 5: Basic input/output
name = input("Enter your name: ")
print("Hello,", name)

# Introduction to control structures
# Control structures like if statements and loops allow you to control the flow of your program.
age = int(input("Enter your age: "))
if age >= 18:
    print("You're an adult.")
else:
    print("You're a minor.")

# Writing functions
# Functions are reusable blocks of code. They can accept arguments and return values.


def greet(name):
    return "Hello, " + name + "!"


print(greet("Bob"))

# Example problem: FizzBuzz - Print numbers from 1 to 100, but for multiples of 3, print "Fizz", for multiples of 5, print "Buzz", and for multiples of both, print "FizzBuzz".
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# Example problem: Factorial - Write a function to calculate the factorial of a given number.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
