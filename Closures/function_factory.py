# Function Factory in Python: A function factory is a function that returns another function. It is used to create functions with specific behaviors or configurations. Here's an example:

def multiplier_factory(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier_factory(2)
triple = multiplier_factory(3)

print(double(5)) # Output: 10
print(triple(5)) # Output: 15

