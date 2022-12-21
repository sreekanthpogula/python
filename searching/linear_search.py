def linear_search(alist, key):
    """returns the index of the given key. Returns the -1 if no such key"""
    for i in range(len(alist)):
        if alist[i] == key:
            return i
    return -1


alist = input('Enter a list of numbers:')
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input('Enter a key:'))

index = linear_search(alist, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at {}-th index.'.format(key, index))
