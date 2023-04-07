# __add__: The __add__ method is used to define the behavior of the + operator for an object.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(2, 3)
v3 = v1 + v2
print(v3.x, v3.y)







