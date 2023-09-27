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
# %%
# My solution
import re
from functools import reduce

document = re.findall(r'\b\w+\b', open('./Data/enchantedForest.txt').read())

uniques = list(set(document))

freq_of_word = dict.fromkeys(uniques)

for key in freq_of_word:
    freq_of_word[key] = len(list(filter(lambda word: word == key, document)))

# Intended approach
document = {
    'Document1': re.findall(
        r'\b\w+\b', open('./Data/enchantedForest.txt').read()
    )
}


def combine_pairs(acc, pair):
    key, value = pair
    if not acc:
        return [(key, int(value))]

    # find the index of the key if it exists in the accumulator
    for i, (acc_key, acc_value) in enumerate(acc):
        if acc_key == key:
            acc[i] = (key, acc_value + int(value))
            break
    else:
        acc.append((key, int(value)))

    return acc


mapped = list(map(lambda x: (x, 1), document['Document1']))
reduced = reduce(combine_pairs, mapped, [])

print(reduced)

# %% [md]
# # Exercise 3 - Inverted Index
# %%

import re
from functools import reduce

documents = {
    1: re.findall(r'\b\w+\b', open('./Data/Story1.txt').read()),
    2: re.findall(r'\b\w+\b', open('./Data/Story2.txt').read()),
}

mapped = []
for i in documents.items():
    print(i[0])
    mapped.extend(list(map(lambda x: (x, i[0]), i[1])))
print(mapped)


def merge_lists_tupl(acc, pair):
    word, doc_id = pair
    for i, (existing_word, doc_ids) in enumerate(acc):
        if word == existing_word and doc_id not in doc_ids:
            acc[i] = (word, doc_ids + [doc_id])
            break
    else:
        acc.append((word, [doc_id]))
    return acc


reduced_tuple = reduce(merge_lists_tupl, mapped, [])
print(reduced_tuple)

# %% [md]
# # Exercise 4 - Euler Tour
# %%
import numpy as np

init_matrix = np.loadtxt('./Data/eulerGraphs1.txt')
graph = np.unique(init_matrix, axis=0).tolist()

vertices = list(set(reduce(lambda x, y: x + y, graph)))


# For every vertice in vertices check map all occurences in all lists in graph
# If it is contained do 1 else 0.
# then reduce it to get the total count pr vertices
degrees = list(
    map(
        lambda v: reduce(
            lambda x, y: x + y, map(lambda e: 1 if v in e else 0, graph)
        ),
        vertices,
    )
)

# Count the number of vertices with even and odd degrees
even = reduce(
    lambda acc, degree: acc + 1 if degree % 2 == 0 else acc, degrees, 0
)
odd = reduce(
    lambda acc, degree: acc + 1 if degree % 2 != 0 else acc, degrees, 0
)

print(even)
print(odd)
# %% [md]
# # Exercise 5 - Common Friends
# %%

from functools import reduce


def split(line):
    friend = line.split(':')
    friends = list(map(int, friend[1].split(',')))
    return (int(friend[0]), friends)


lines = list(map(split, open('./Data/friends2.txt').readlines()))
mapped = []
for i in lines:
    mapped.extend(list(map(lambda y: (sorted([i[0], y]), i[1]), i[1])))


def merge_lists_tuple(acc, pair):
    friend_pair, friends = pair
    for i, (existing_pair, existing_friends) in enumerate(acc):
        if friend_pair == existing_pair:
            acc[i] = (
                friend_pair,
                list(filter(lambda x: x in existing_friends, friends)),
            )
            break
    else:
        acc.append((friend_pair, friends))
    return acc


reduced = reduce(merge_lists_tuple, mapped, [])
print(reduced)

# %% [md]
# # Exercise 6 - Triangle Counting
# %%

# Just a stupid non reduce/map version
import numpy as np
import numba
from functools import reduce

filename = './Data/roadnet.txt'

neighbors = dict()

# Read the file and populate the neighbors dictionary
with open(filename, 'r') as file:
    for line in file:
        edge = line.strip().split()
        node1, node2 = int(edge[0]), int(edge[1])

        # Add nodes to the neighbors dictionary
        if node1 not in neighbors:
            neighbors[node1] = set()
        if node2 not in neighbors:
            neighbors[node2] = set()

        # Add edges to the neighbors dictionary
        neighbors[node1].add(node2)
        neighbors[node2].add(node1)
print(len(neighbors))
# Function to count triangles for a given node
def count_triangles_for_node(node, neighbors):
    triangle_count = 0
    node_neighbors = neighbors[node]

    for neighbor1 in node_neighbors:
        for neighbor2 in node_neighbors:
            if neighbor1 < neighbor2 and neighbor2 in neighbors[neighbor1]:
                triangle_count += 1

    return triangle_count


# Iterate through nodes and count triangles
def test():
    total_triangles = 0
    for node in neighbors:
        total_triangles += count_triangles_for_node(node, neighbors)

    # Divide by 3 because each triangle is counted 3 times
    return total_triangles / 3


print('Number of triangles in the graph:', test())

# %% [md]
# # Exercise 7 - NetworkX
# This is legit just a faster way to fix to do it with dedicated functions for graph theory
