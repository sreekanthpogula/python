# Python Functions is a block of statements that return the specific task.
import re
from datetime import datetime


def fun():
    print("welcome to python")


fun()


def add_sum(num1, num2):
    sum = num1 + num2

    return sum


res = add_sum(2, 3)
print(res)


def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
        return True


print(is_prime(78), is_prime(79))


def even_odd(n):
    if (n % 2 == 0):
        print("even")
    else:
        print("odd")


even_odd(2)
# default arguments


def myFun(x, y=50):
    print("x:", x)
    print("y:", y)


myFun(10, 20)


def student(first_name, last_name):
    print(first_name, last_name)


student(first_name='sreekanth', last_name='pogula')


def myfun1(*argv):
    for arg in argv:
        print(argv)


myfun1('hello', 'welcome')


def my_fun():
    yield


for value in my_fun():
    print(value)


def my_decorator_func(func):

    def wrapper_func():
        print("before the function is called")
        func()
        # Do something after the function.
        print("after the function is called")
    return wrapper_func


@my_decorator_func
def my_func():

    pass

# simple decorator function in python


def log_datetime(func):
    '''Log the date and time of a function'''

    def wrapper():
        print(
            f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper


@log_datetime
def daily_backup():

    print('Daily backup job has finished.')


daily_backup()

# practice of decorator


def my_first_decorator_fun(func):
    """my first decorator function"""
    def my_first_wrapper_fun():
        print(5+5)
    func()
    print(20+5)
    return my_first_wrapper_fun


@my_first_decorator_fun
def my_fun():
    print(5-5)


my_fun()

# decorator chaining


def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner


@decor1
@decor
def num():
    return 10


print(num())

# iterator in python
a = "sreekanth"
a_iterator = iter(a)

for i in a_iterator:
    print(i)

# Sample built-in iterators
# iterating over a list
a = [1, 2, 3, 4, 5]

for i in a:
    print(i)

# iterating over a tuple(immutable)
t = (1, 4, 5, 6)
for i in t:
    print(i)

# iterating over a string
str = "sreekanth"
for i in str:
    print(i)

# iterating over dictionary
d = {"a": 1, "b": 2, "c": 3}
for i in d:
    print(i, d[i])

# iterable vs iterator
# iterable

# iterating on an iterator

    # Getting StopIteration Error while using iterator
item_1 = (1, 2, 3, 4, 5)
iter_obj = iter(item_1)
for item in iter_obj:
    print((item))
# loops in python
# if loop
if (5 < 1):
    print("im in")
print("im out")
# if-else loop
if (5 > 1):
    print("im in")
else:
    print("im out")
# nested if loop
if (10 > 1):
    print("im sree")
    if (10 < 2):
        print("im vikki")

# if-elif - else ladder
if (10 < 2):
    print("im a human")
elif (10 < 2):
    print("im viking")
else:
    print("im sreekanth")

# if else shorthand
i = 10
print(True) if i < 15 else print(False)

# mapping in python


def addition(num):
    return num + num


numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# double all numbers using map and lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# add two lists using map and lambda
num1 = [1, 2, 3, 4]
num2 = [2, 4, 6, 8]
result = map(lambda x, y: x + y, num1, num2)
print(list(result))

# list of strings
l = ["sreekanth"]
test = list(map(list, l))
print(test)

# regex in python
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("yes we have a match")
else:
    print("no match")
# findall
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
# split
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
# sub
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# file handling
text_file = open('file.txt', 'r')

# another  method using full operation
text_file2 = open('../file.txt', 'r')
print('First Method')
print(text_file)

print('Second Method')
print(text_file2)

text_file = open('./abc.txt', 'r')
line_list = text_file.readlines()
for i in line_list:
    print(line_list)

text_file.close
# read mode
file = open("file.txt", "r")
print(file.read())
# write mode
file = open("file.txt", "w")
file.write("this is the write command")

file.close()

# exception handling
# amount = 10000
# if (amount > 2999):
# print("you are elgible for the purchase of dsa course")

marks = 10000
try:
    a = marks/1
    print(a)
except ZeroDivisionError:
    print("can't divide by zero")
finally:
    print('this is always executed')

try:
    raise NameError("hi there")
except NameError:
    print("an exception")
    raise
