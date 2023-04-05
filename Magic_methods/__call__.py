#__call__: The __call__ method is used to make an object callable like a function.
class Adder:
    def __init__(self, num):
        self.num = num
        
    def __call__(self, x):
        return self.num + x

adder = Adder(10)
print(adder(5)) # Output: 15


