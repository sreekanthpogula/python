# # datatypes in pythons
# # integer data type - integer, float, complex
# a = 4  # integer
# money = 3.0  # float
# n = 100 + 3j  # complex
# print(type(a), a)
# print(type(money), money)
# print(type(n), n)
#
# # string data type - string
# s = "string in double quotes"
# print(type(s), s)
# a = 'string in single quotes'
# print(type(a), a)
# print(s + " " + a)
#
# # list data type - list
# list1 = [1, 2, 3]
# print(type(list1), list1)
# list2 = [1.0, 2.0, 3.0, "hello world"]
# print(type(list2), list2)
# print(list1 + list2)
# print(list1[0])
# print(list1[2])
#
# # tuple data type - tuple
# tuple1 = (1, 2, 3)
# print(type(tuple1), tuple1)
# tuple2 = (1.0, 2.0, 3.0, "hello world")
# print(type(tuple2), tuple2)
# print(tuple1[0])
# # dictionary -data type
# dict1 = {"a": 1, "b": 2, "c": 3}
# print(type(dict1), dict1)
# dict2 = {"a": 1.0, "b": 2.0, "c": 3.0}
# print(type(dict2), dict2)
# print(dict1["c"])
# print(dict1["b"])
#
# x = "Hello, world!"  # string representation
# y = 20  # integer representation
# a = 20.5  # float representation
# real_number = 1 + 29j  # complex number representation
# fruits = ["apple", "orange", "banana"]  # list representation
# vegetables = ("tomato", "carrot", "cabbage")  # tuple representation
# distance = range(5)  # range representation
# dict1 = {"a": 1, "b": 2, "c": 3}  # dictionary representation
# team = {"apple", "banana", "cherry"}  # set representation
# bread = frozenset({"apple", "banana", "cherry"})  # frozenset representation
# b = True  # boolean representation
# z = b"Hello"  # byte representation
# c = bytearray(5)  # bytearray representation
# m = memoryview(bytes(5))  # memory view representation
# d = None  # None representation
#
#
# # Fibonacci series using python
# def fib(number):
#     result = []
#     i, j = 0, 1
#     while i < number:
#         result.append(i)
#         i, j = j, i + j
#     return result
#
#
# f100 = fib(2000)
# print(f100)
#
#
# # factorial of a number in python
# def factorial(number1):
#     if number1 == 0:
#         return 1
#     else:
#         return number1 * factorial(number1 - 1)
#
#
# print(factorial(5))
#
#
# # def argument values
# def ask_ok(prompt, retries=4, remainder='please try again'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nope'):
#             return False
#         retries = retries + 1
#         if retries < 0:
#             raise Exception('too many retries')
#         print(remainder)
#
#
# ask_ok('Do you really want to quit?')from poetry.console.commands import self


def ask_yes(prompt):
    while True:
        print(prompt)


def function():
    pass


def fun(number):
    print(number)


fun(5)


def firstname(f_name):
    print(f_name + " " + "is hero")


firstname("pavan")


def children(*kids):
    print(kids[0:2])


children("vikki", "verra")


def my_function(child3, child2, child1):
    print("The youngest child is " + child1)


my_function(child1="Emil", child2="Tobias", child3="Linus")
z = lambda k: k + 10
print(z(5))


def make_incermentor(number2):
    return lambda x: x + number2


f = make_incermentor(43)
print(f(5))

# iterator in python
# s = 'abc'
# it = iter(s)
# print(next(it))
# print(next(it))
# print(next(it))
#
# # reverse program using iterators in python
#
#
# class Reverse:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index -= 1
#         return self.data[self.index]
#
#
# rev = Reverse('sreekanth')
# iter(rev)
# for char in rev:
#     print(char)


# Generators in python
"""Generator-Function: A generator-function is defined like a normal function,
 but whenever it needs to generate a value, it does so with the yield keyword rather than return. 
 If the body of a def contains yield, the function automatically becomes a generator function."""


def generator_fun():
    yield 2
    yield 4
    yield 6


for value in generator_fun():
    print(value)


#  decorators are used to modify the behaviour of function or class.
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.


def shout(text):
    return text.upper()


print(shout('Hello'))

yell = shout

print(yell('Hello'))
