# Data structure in python are used organize, manage, and storing data in python.

# types of data structures in python
# Built-in types of data structures
# List are used to store data of different data types in a sequential manner. There are addresses assigned to every element of the list, which is called as Index. The index value starts from 0 and goes on until the last element called the positive index. There is also negative indexing which starts from -1 enabling you to access elements from the last to first.
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list1 = [1, 2, 3, 4, 5, 'example', 3.21]
print(my_list1)
my_list.append([my_list1])
print(my_list)
my_list.extend([234, 'more', 'example'])
print(my_list)
my_list.insert(1, 'example')
print(my_list)
del my_list[4]
print(my_list)
my_list.remove('example')
print(my_list)
a = my_list.pop(1)
print(a)
my_list.clear()
print(my_list)

# Accessing the list items
my_list = [1, 2, 3, 'example', 3.132, 10, 30]
for i in my_list:
    print(i)  # iterate  over the list
print(my_list)  # access all the items
print(my_list[3])  # access index 3 element
print(my_list[0:2])  # access index 2 element
print(my_list[::-1])  # access index 1 element
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(my_list))
print(my_list.index(1))
print(my_list.count(9))
print(sorted(my_list))

# Tuple
# Dictionary
# Set
# User-defined types of data structures
# Stack
# Queue
# Tree
# Linked list
# Graph
# HashMap
