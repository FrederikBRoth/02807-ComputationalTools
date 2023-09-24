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
print('awd')
