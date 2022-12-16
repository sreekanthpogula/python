"""Reference counting works by counting the number of times an
object is referenced by other objects in the system. When references to an object are removed, the reference count for ,
an object is decremented. When the reference count becomes zero, the object is deallocated."""
x = 10
y = x
if id(x) == id(y):
    print("x and y are equal")


x = 10
y = x
x += 1
if id(x) != id(y):
    print("x and y are not equal")

# There are two parts of memory:
# The methods/method calls and the references are stored in stack memory
# and all the values objects are stored in a private heap.
# stack memory
def func():
    a = 20
    b = []
    c = ""

# heap memory
a = [0] * 10
