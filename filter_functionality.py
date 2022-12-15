# filter(function, iterable)
numbers = [-2, 3, 4, 5, 6]
positive_numbers = filter(lambda n: n < 0, numbers)
print(positive_numbers)
print(list(positive_numbers))

# palindrome


def palindrome(word):
    reversed_word = "".join(reversed(word))
    return word.lower() == reversed_word.lower()


words = ("filter", "Ana", "hello", "world", "madam", "racecar")
print(list(filter(palindrome, words)))
