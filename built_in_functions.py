# Python abs() Function Example
a = -23
print(abs(a))

# Python all() Function in Python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(all(l))
l = [1, 2, 3, 4, 5, False, 7, 8, 9]
print(all(l))

# python any() function
l = [False, 2, True, False, False]
print(any(l))

# python bin() function
a = 3
print(bin(a))

# python bool() function
a = True
print(bool(a))

# python bytearray() function
x = bytearray(2)
print(bytearray(x))

# python bytes() function
x = bytes(4)
print(bytes(x))

# python callable() function


def x():
    a = 5


print(callable(x))

# python chr() function
x = chr(97)
print(x)

# class method() function in python


class geeks:
    course = 'DSA'

    def purchase(object):
        print("purchase course : ", object.course)


geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()
