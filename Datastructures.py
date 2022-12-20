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
my_tuple = (1, 2, 3, 'education')  # creating a tuple
print(my_tuple)
for x in my_tuple:
    print(x)
print(my_tuple[0])
print(my_tuple[:])
print(my_tuple[3][4])
my_tuple = my_tuple + (4, 5, 6)
print(my_tuple)
print(my_tuple.count(2))
# Dictionary
my_dict = {}
print(my_dict)
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)
# Changing and Adding key, value pairs
my_dict = {"first": 1, "second": 'python', "third": 'Java'}
print(my_dict)
my_dict['second'] = 'c++'
print(my_dict)
my_dict['third'] = 'rust'
print(my_dict)
# Deleting key, value pairs
a = my_dict.pop('third')
print('value:', a)
print('dictionary:', my_dict)
b = my_dict.popitem()
print('key', 'value pair:', b)
print('dictionary:', my_dict)
my_dict.clear()
print(my_dict)
# accessing dictionary
my_dict = {'first': 'rust', 'second': 'java', 'third': 'go'}
print(my_dict['first'])
print(my_dict.get('second'))
print(my_dict.keys())  # get all keys
print(my_dict.values())  # get key-value pairs
print(my_dict.items())


# Set
my_set = {1, 2, 3, 4, 5, 4, 7, 8, 9}  # create set
print(my_set)
# adding elements
my_set.add(10)  # add elements to set
print(my_set)
my_set_2 = {1, 2, 3, 4, 5}
print(my_set.union(my_set), '-------------', my_set | my_set_2)
print(my_set.intersection(my_set_2), '--------', my_set & my_set_2)
print(my_set.difference(my_set_2), '----------', my_set - my_set_2)
print(my_set.symmetric_difference(my_set_2), '----------', my_set ^ my_set_2)
my_set.clear()
print(my_set)


# User-defined types of data structures
# Stack
# Queue
# Tree
# Linked list
# Graph
# HashMap
