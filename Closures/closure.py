# Closure in Python:In Python, a closure is created when a nested function (function defined inside another function) accesses a variable from its enclosing lexical scope. When the outer function completes execution, the inner function retains a reference to the variables of the outer function, creating a closure over those variables. Here's an example:

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure_func = outer_function(5)
print(closure_func(3))