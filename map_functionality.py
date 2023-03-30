# map function in python
# map(function, iterator1,iterator2 ...iteratorN)
def square(n):
    return n * n


my_list = [2, 3, 4, 5, 6, 7, 8, 9]
updated_list = map(square, my_list)
print(updated_list)
print(list(updated_list))

# using map with python built-in functions
my_list = [2.6743, 3.63526, 4.2325, 5.9687967, 6.3265, 7.6988, 8.232, 9.6907]
updated_list = map(round, my_list)
print(updated_list)
print(list(updated_list))
# Using map() with a string as an iterator


def myMapFunc(s):
    return s.upper()


my_str = "welcome to Senecaglobal!"
updated_list = map(myMapFunc, my_str)
print(updated_list)
for i in updated_list:
    print(i, end="")

# using map() with the lambda function
my_list = [2, 3, 4, 5, 6, 7, 8, 9, 0]
updated_list = map(lambda x: x * 10, my_list)
print(list(updated_list))
