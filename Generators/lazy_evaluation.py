# Lazy evaluation is a programming technique in which the evaluation of an expression is delayed until its value is actually needed. This can be useful for improving the performance of programs, especially when dealing with large data sets or complex computations.

# In lazy evaluation, expressions are not evaluated immediately when they are created, but are instead stored in a data structure such as a thunk or a promise. When the value of the expression is eventually needed, the thunk or promise is "forced" to evaluate the expression and return its value. This can reduce the amount of unnecessary computation that is performed, because only the parts of the program that are actually used are evaluated.

#Sample program
# Define a function that generates a sequence of Fibonacci numbers
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Define a generator expression that generates the first 10 Fibonacci numbers
fibonacci_sequence = (n for i, n in enumerate(fibonacci()) if i < 10)

# Print the first 10 Fibonacci numbers
for n in fibonacci_sequence:
    print(n)
