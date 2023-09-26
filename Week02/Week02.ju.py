# %% [md]
# # Week 2 - Exercises
# Exercise 1
#
# [map, filter, reduce documentation](https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce)
#
# This is the map function in python. Map applies a function on all elements in the list and results in a new changed list
# %%
# shitty way
credit_cards = [913, 113, 513, 173, 645, 654]

newlist = []

for card in credit_cards:
    card_ = card + 1000
    newlist.append(card_)

print(newlist)

# Cool way

new_cool = list(map(lambda x: x + 2000, credit_cards))
print(new_cool)

# You can pass as many arguments as the functions can take

new_new_cool = list(map(lambda x, y: x + y + 1000, credit_cards, range(1, 10)))
print(new_new_cool)
# %% [md]
# Filter function
# Filter function tldr:
# 1. Unlike map(), only one iterable is required.
# 2. The func argument is required to return a boolean type. If it doesn't, filter simply returns the iterable passed to it. Also, as only one iterable is required, it's implicit that func must only take one argument.
# 3. filter passes each element in the iterable through func and returns only the ones that evaluate to true. I mean, it's right there in the name -- a "filter".
# %%

# Example

dank_meme = [85, 69, 420, 20, 22]


def is_meme(id):
    return id == 85 or id == 420 or id == 69


real_memes = list(filter(is_meme, dank_meme))
print(real_memes)

# You can do lambdas aswell

dromes = ['bob', 'nothing', 'anutforajaroftuna', 'rewire']

test = 'yooo'
reversed = test[::-1]
print(reversed)

# FYI you can do lists like [<start>:<stop>:<step>]
palindromes = list(filter(lambda word: word == word[::-1], dromes))
print(palindromes)

# %% [md]
# Reduce function
# Can take a list and iteratively add the elements together (or somethign else, depending on the function)
# %%
from functools import reduce

abc = ['a', 'b', 'c', 'd']
together = reduce(lambda a, b: a + b, abc)
print(together)

# %% [md]
# Exercise in map, filter and reduce
# %%
from functools import reduce
import numpy as np

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ['olumide', 'akinremi', 'josiah', 'temidayo', 'omoseun']

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: round(np.square(x), 3), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)
# %% [md]
# # Exercise 2 - Word Frequency
#
