# Python has a set of built-in methods that you can use on strings.
import re
a = 'sreekanth'
x = a.capitalize()
print(x)
b = a.casefold()
print(b)
c = a.center(2)
print(c)
d = a.count('e')
print(d)
txt = "My name is Sreekanth."

x = txt.encode()

print(x)

e = a.endswith('.')
print(e)
# string concatenation
word1 = 'New'
word2 = 'York'
print(word1 + " " + word2)

word = 'Rio de Janeiro'
char = word[0:4]
print(char)

# size of the string
print(len('RIO'))
print(len('RIO de Janeiro'))
# Replace the part of a string
# print('RIO de Janeiro'.replace('rio', 'amer'))
word = 'rio de janeiro'
print(word.count('e'))

# repeat the string
words = 'Tokyo' * 3
print(words)

# Split the string in python
my_phrase = "let's; g.o to; th/e beach/h"
my_words = my_phrase.split("/")
for word in my_words:
    print(word)
print(my_words)
print(my_words[2])

# removing all the white spaces in the string
phrase = 'Do  you  want  to  try  again'
phrase_no_space = re.sub(r'\s+', '', phrase)
print(phrase)
print(phrase_no_space)

# How to Handle Multiline Strings in Python
long_text = """this is a multiline string that contains  a number of characters that are not allowed in Python"""
print(long_text)

# using single quotes
long_text = '''this is a multiline string that contains a number of characters that are not allowed in Python'''
print(long_text)

# using parenthesis
long_text = ("this is a multiline string, \n\n"
             "that contains a number of characters")
print(long_text)

# Backslashes
long_text = "this is a multiline string, \n\n" \
    "that contains a number of, \n\n" \
    "that contains  a number of"
print(long_text)

# lstrip() used to remove whitespace and characters from the beginning of the string
regular_text = "  This is a regular expression text"
no_space_begin_text = regular_text.lstrip()
print(regular_text)
print(no_space_begin_text)

# to remove chars
regular_text = "$@G#This is a regular expression."
clean_begin_text = regular_text.lstrip("#@G$")
print(regular_text)
print(clean_begin_text)

# how to remove whitespace and characters from the end of the string
regular_text = "This is a regular text.   "

no_space_end_text = regular_text.rstrip()

print(regular_text)
#'This is a regular text.   '

print(no_space_end_text)
#'This is a regular text.'

# how to remove spaces and characters from the beginning and end of string
regular_text = " this is a regular text  "
no_space_text = regular_text.strip()
print(regular_text)
print(no_space_text)
# How to Make a Whole String Lowercase in Python
regular_text = "THIS IS A WHOLE CAPITAL STRING"
regular_lower = regular_text.lower()
print(regular_text)
print(regular_lower)

# How to Make a Whole String uppercase in Python
regular_text = "this is a who is a who is a"
regular_lower = regular_text.upper()
print(regular_text)
print(regular_lower)

# How to Use Title Case in Python
regular_text = "this is a who is a who is"
title_text = regular_text.title()
print(regular_text)
print(title_text)
# How to Use Swap Case in Python
regular_text = "This is a Who is a who is"
swap_case_text = regular_text.swapcase()
print(regular_text)
print(swap_case_text)
# How to Check if a String is Empty in Python
my_string = 'raff'
if not my_string:
    print("Empty string")

# How to Check if a String is not Empty in Python
my_string = 'raff'
if my_string:
    print("not an Empty string")
# rjust(): How to Right-justify a String in Python
word = 'beach'
number_spaces = 10
word_justified = word.rjust(number_spaces)
print(word)
print(word_justified)
# ljust(): How to left-justify a String in Python
word = 'beach'
number_spaces = 10
word_justified = word.ljust(number_spaces)
print(word)
print(word_justified)

word = 'beach'
number_spaces = 10
char = '$'
word_justified = word.rjust(number_spaces, char)
print(word)
print(word_justified)

# isalnum(): How to Check for Alphanumeric Characters Only in a String in Python
word = 'beach'
print(word.isalnum())
word = '32'
print(word.isalnum())
word = 'number32'
print(word.isalnum())
word = 'string is 32'
print(word.isalnum())
word = 'string is @1435#$'
print(word.isalnum())
# isprintable(): How to Check for Printable Characters in a String in Python
text = ''
print(text.isprintable())
text = 'this is a regular string'
print(text.isprintable())
text = ' '
print(text.isprintable())
text = '            '
print(text.isprintable())
text = '\f\n\r\t\v'
print(text.isprintable())

# isspace(): How to Check for White Space Only in a String in Python
text = ''
print(text.isspace())
text = 'ewe edwy'
print(text.isspace())
# startswith(): How to Check if a String Begins with a Certain Value in Python
word1 = "sreekanth is a reserved word"
print(word1.startswith('s'))
print(word1.startswith('q'))

# position based search
word1 = "sreekanth is a reserved word"
print(word1.startswith('siree', 0))
print(word1.startswith('ieee', 0))
# capitalize(): How to Set the First Character Only to Upper Case in a String in Python
text = 'this is the regular text'
print(text.capitalize())

# isupper(): How to Check for Upper Case Only in a String in Python
text = 'this is the regular text'
print(text.isupper())

text = 'THIS IS A REGULAR TEXT'
print(text.isupper())
# join(): How to Join Items of an Iterable into One String in Python
my_string = 'siree'
print('$'.join(my_string))

my_list = ['bmw', 'ferrari', 'mclaren']
print('$'.join(my_list))

my_tuple = ('bmw', 'ferrari', 'mclaren')
print('$'.join(my_tuple))

my_set = {'bmw', 'ferrari', 'mclaren'}
print('$'.join(my_set))


my_dict = {'bmw': 'BMW', 'ferrari': 'ferrari', 'mcl': 'mclaren'}
print('$'.join(my_dict))
# splitlines(): How to Split a String at Line Breaks in Python
my_txt = 'Thank you for the \n music Welcome to the jungle'
x = txt.splitlines(True)
print(x)
# islower(): How to Check for Lower Case Only in a String in Python
text = 'this is the first time you have seen this song in this'
print(text.islower())

text = 'This is a regular text'
print(text.islower())

# isnumeric(): How to Check for Numerics Only in a String in Python
word = '32'
print(word.isnumeric())

word = 'wfwe'
print(word.isnumeric())
# isdigit(): How to Check for Digits Only in a String in Python
word = '32'
print(word.isdigit())

word = 'beach'
print(word.isdigit())

word = '@32$'
print(word.isdigit())

# isdecimal(): How to Check for Decimals Only in a String in Python
word = '32'
print(word.isdecimal())
word = 'wdwwd'
print(word.isdecimal())

# isalpha(): How to Check for Letters Only in a String in Python
word = 'beach'
print(word.isalpha())

word = 'be232'
print(word.isalpha())
# istitle(): How to Check if Every Word Begins with an Upper Case Char in a String in Python
text = 'This is a regular text'
print(text.istitle())

text = 'This Is A Regular Text'
print(text.istitle())
# expandtabs(): How to Set the Number of Spaces for a Tab in a String in Python
my_string = 'B\tR'

print(my_string.expandtabs())

my_string = 'WORL\t'

print(my_string.expandtabs())
# Custom Tabsize
my_string = 'B\tR'

print(my_string.expandtabs(4))
# center(): How to Center a String in Python
word = 'beach'
number_spaces = 32

word_centered = word.center(number_spaces)

print(word)
print(word_centered)
# zfill(): How to Add Zeros to a String in Python
word = 'beach'
size_string = 32

word_zeros = word.zfill(size_string)

print(word)
print(word_zeros)

# find(): How to Check if a String Has a Certain Substring in Python
phrase = "This is a regular text"

print(phrase.find('This'))
print(phrase.find('a'))
print(phrase.find('ded'))
# How to Remove a Prefix or a Suffix in a String in Python
print('Rio de Janeiro'.removeprefix("Rio"))
print('Rio de Janeiro'.removesuffix("eiro"))

# lstrip() vs removeprefix() and rstrip() vs removesuffix()
word = 'hubfefefekfel'
word = word.lstrip('hub')
print(word)

word = word.removeprefix('rio')
print(word)

word = word.rstrip('hub')
print(word)

word = word.removesuffix('rio')
print(word)
# python slicing - list[start:stop:step]
word = 'sreekanth'
sliced = word[0:4]
print(sliced)

# How to Reverse a String in Python
my_string = 'sreekanth'
my_string_reverse = my_string[::-1]
print(my_string)
print(my_string_reverse)
