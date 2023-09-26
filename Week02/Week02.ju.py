# %% [md]
## This is the assignments for 1.
# 1.1.1 - Hello world
# %%
for _ in range(10):
    print('Hdllo, world!')
# %% [md]
# 1.1.6 - useargument modif
# %%
import sys

name1 = input()
name2 = input()
name3 = input()
print(name1, name2, name3)
# %% [md]
# 1.2.2 - cos sin aprox 0.0
# %%
import math

number = int(input())
result = math.pow(math.cos(number), 2) + math.pow(math.sin(number), 2)
print(result)
# %% [md]
# Skipping 1.2.5 and 1.2.8 because of simple type relationship tests.
# Types change based on what is added to what.
#
# 1.2.11 - Simple Modulus
# %%

input1 = int(input())
input2 = int(input())

if input1 % input2 == 0 or input2 % input1 == 0:
    print(True)
# %% [md]
# 1.3.6
# %%
amount = int(input())
i = 0
while i <= amount:
    if i % 10 == 1 and i != 11:
        print(str(i) + 'st Hello')
    elif i % 10 == 2 and i != 12:
        print(str(i) + 'nd Hello')
    elif i % 10 == 3 and i != 13:
        print(str(i) + 'rd Hello')
    else:
        print(str(i) + 'th Hello')
    i = i + 1
# %% [md]
# 1.3.7
# %%
for i in range(1000, 2000):
    print(str(i), end='')
    if (i + 1) % 5 == 0:
        print('\n')

# %% [md]
# 1.3.13
# %%

import math

input1 = int(input())

if input1 > 0:
    i = 0
    powNumber = 0

    while powNumber < input1:
        powNumber = math.pow(i, 2)
        if powNumber < input1:
            print(str(i) + ' to the power of 2 is ' + str(powNumber))
        i = i + 1
# %% [md]
# 1.3.27
# %%

inl = int(input())

for i in range(0, inl):
    string = ''
    for j in range(0, inl):
        if i % 2 != 0:
            string += ' *'
        else:
            string += '* '

    print(string)
# %% [md]
# 1.4 Creative 2 - Longest Plateau
# %%
import numpy as numpy

arr = [1, 2, 2, 2, 3, 3, 3, 3, 3, 6, 2, 1, 1]


def longest_plateau(arr):
    max_length = 0  # Length of the longest plateau found so far
    max_start = -1  # Starting index of the longest plateau found so far
    current_length = 1  # Length of the current plateau
    current_start = 0  # Starting index of the current plateau

    for i in range(1, len(arr)):
        if (
            arr[i] == arr[i - 1]
        ):  # Check if the current element is equal to the previous one
            current_length += 1
        else:
            if (
                i > 1 and arr[i] < arr[i - 2]
            ):  # Check if the current element is smaller than the one before it
                if current_length > max_length:
                    max_length = current_length
                    max_start = current_start
            current_length = 1
            current_start = i

    # Check one more time after the loop in case the longest plateau ends at the end of the array
    if current_length > max_length:
        max_length = current_length
        max_start = current_start

        return max_length, arr[max_start : max_start + max_length]


print(longest_plateau(arr))
# %% [md]
# 1.4 Creative 10 - Find Duplicates
# %%
list = [1, 2, 3, 4, 5, 5, 6, 7]


def find_duplicate(list):
    for idx, i in enumerate(list):
        for jdx, j in enumerate(list):
            if j == i and idx != jdx:
                return 'Duplicate found!'
                break
    return 'No duplicates!'


print(find_duplicate(list))
# %% [md]
# 2.3 - Recursion
# %%


def ex233(n):
    if n <= 0:
        return
    print(n)
    ex233(n - 2)
    ex233(n - 3)
    print(n)


ex233(6)
# %% [md]
# 2.3 Creative 3 - Permutations
# %%
def perm(s):
    if len(s) == 0:
        return ['']

    strings = []
    for i in range(len(s)):
        # Compute a list of permutations of s with s[i] removed.
        subStrings = perm(s[:i] + s[i + 1 :])

        # Prepend s[i] to each string in that list.
        for subString in subStrings:
            strings += [s[i] + subString]

    return strings


print(perm(['a', 'b', 'c']))
# %% [md]
# # NumPy package
# Exercises about numpy
# %%
import numpy as np

matrix = np.loadtxt('numpyMatrix.txt', usecols=range(4))
A = matrix[:, :-1]
b = matrix[:, -1]

# Solve the linear equation Ax = b
x = np.linalg.solve(A, b)

print('Solution x:')
print(x)
# %% [md]
# # SciPy Package
# Exercises about SciPy
# %%

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

array = np.loadtxt('scipymatrix.txt')
x = np.array(array[:, 0])
y = np.array(array[:, -1])
print(x)
print(y)

coefficients = np.polyfit(x, y, 3)
poly = np.poly1d(coefficients)

print(coefficients)
print(poly)


def polynomial_function(x):
    return poly(x)


roots = []
x_intervals = zip(x[:-1], x[1:])
for interval in x_intervals:
    a, b = interval
    fa = polynomial_function(a)
    fb = polynomial_function(b)

    if fa * fb < 0:  # Check if f(a) and f(b) have different signs
        root = root_scalar(polynomial_function, bracket=[a, b])
        if root.converged and root.root.imag == 0:
            roots.append(root.root.real)


x_range = np.linspace(min(x), max(x), 100)
y_range = poly(x_range)

plt.plot(x_range, y_range, label='Fitted Polynomial')
plt.scatter(roots, [0] * len(roots), color='red', marker='o', label='Roots')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Fitted Polynomial and Its Roots')
plt.grid(True)
plt.show()

# Print the roots
print('Real roots of the polynomial:', roots)
# %% [md]
# # Numba Package
# Exercises about Numba
# %%
from numba import njit
import numpy as np
import math


def sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / np.power(i, 2)


n = 10000
# %timeit -r 1 -n 100 sum(n)


@njit
def ssum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / np.power(i, 2)


n = 10000
# %timeit -r 1 -n 2000 ssum(n)
# %% [md]
# # Pandas Package
# Exercies about Pandas
# [Scraping](https://towardsdatascience.com/scraping-tabular-data-with-pandas-python-10cf2a133cbf)
# %%
import pandas as pd

pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

url = 'https://en.wikipedia.org/wiki/The_World%27s_Billionaires'

df_list = pd.read_html(url)
print(df_list[2])
