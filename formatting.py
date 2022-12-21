# String formatting is the process of infusing things in the string dynamically and presenting the string.


# Formatting with % Operator.
from string import Template
print("The mangy, scrawny stray dog %s gobbled down" % 'hurriedly')

x = 'looked'
print("The mangy %s scrawny stray dog %s gobbled down" % ('looked', x))

print('Joe stood up and %s to the crowd.' % 'spoke')

print('There are %d dogs.' % 4)
print('The value of pi is: %5.4f' % (3.141592))
# ‘%s’ is used to inject strings similarly ‘%d’ for integers, ‘%f’ for floating-point values, ‘%b’ for binary format.

# Formatting with format() string method.
print('We all are {}.'.format('equal'))
print('{2} {1} {0}'.format('directions',
                           'the', 'Read'))
print('a: {a}, b: {b}, c: {c}'.format(a=1,
                                      b='Two',
                                      c=12.3))
print(
    'The first {p} was alright, but the {p} {p} was tough.'.format(p='second'))
# Formatting with string literals, called f-strings.
name = 'Ele'

print(f"My name is {name}.")
a = 5

b = 10

print(f"He said his age is {2 * (a + b)}.")
# Formatting with String Template Class
n1 = 'hello'
n2 = 'geeksforgeeks'

n = Template('$n3 !This is a string template of $n4 characters')
print(n.substitute(n3=n1, n4=n2))
