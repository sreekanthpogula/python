# 1. Data Structures - Lists and Tuples

# Lists
my_list = [1, 2, 3, "apple", "banana"]  # creation of list
print(my_list[3])  # Accessing an element
my_list.append("cherry")  # Appending an element
my_list[0] = "cake"  # modifying an element
my_list.remove(2)  # Removing an element
index = my_list.index("cake")  # Index of the element
print(len(my_list))  # Length of the list

# Tuples
my_tuple = (1, 2, "apple")
# my_tuple[0] = 3  # This will result in an error since tuples are immutable

# 2. List Comprehensions
squared_numbers = [x**2 for x in range(1, 6)]
print(squared_numbers)

# 3. Hands-on Exercises with Lists and Tuples
favorite_movies = ["KGF", "Salar", "Baby"]
favorite_movies.append("Bahubali")
print(favorite_movies[1])
fav_fruits = ("orange", "Banana", "cherry")
# fav_fruits[1] = "apple"

favorite_fruits = ("apple", "banana", "orange")
# favorite_fruits[0] = "grape"  # This will result in an error due to immutability

# 4. Dictionaries and Sets
my_dict = {"name": "John", "age": 25, "city": "New York"}
print(my_dict["age"])
my_dict["occupation"] = "Engineer"
del my_dict["city"]

my_set = {1, 2, 3, 3, 4, 5}

# 5. Common Dictionary Operations
value = my_dict[key] # Accessing values
my_dict[new_key] = new_value # Adding a new key-value pair: 
del my_dict[key] # Removing a key-value pair: 
my_dict.pop(key) # Removing a key-value pair: 
for key in my_dict: # Iterating through keys: 
Iterating through values: for value in my_dict.values():
Iterating through key-value pairs: for key, value in my_dict.items():

# 6. Dictionary Comprehensions
squared_dict = {x: x**2 for x in range(1, 6)}
print(squared_dict)

# Exercises
word_lengths = {"apple": 5, "banana": 6}
word_lengths["grape"] = 5
del word_lengths["apple"]

unique_numbers = set([1, 2, 3, 3, 4, 5, 5])
print(unique_numbers)
