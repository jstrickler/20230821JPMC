import operator as op
from functools import reduce

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f1 = map(str.upper, fruits)  # f1 is an *iterator*  (generator-like)
print(f"f1: {f1}\n")
# print(f"f1[0]: {f1[0]}")

fruits.append('mangosteen')
print(f"list(f1): {list(f1)}\n")

f2 = map(str.upper, fruits)
fruit_data = list(f2)  # convert virtual object to actual list
print(f"fruit_data[0]: {fruit_data[0]}")

f3 = [f.upper() for f in fruits]   # list comprehension
print(f"f3[0]: {f3[0]}")
print(f"f3: {f3}\n")

f4gen = (f.upper() for f in fruits)   # generator expression
print(f"f4gen: {f4gen}")

values = [5, 8, 2, 7, 9]

product = reduce(op.mul, values)
print(f"product: {product}\n")


