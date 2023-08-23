from itertools import chain

a = [1, 2, 3]
b = 4, 5, 6
c = 58,   # tuple

for x in chain(a, b, c):
    n = int(x)
    print(n)

data = []
for obj in a, b, c:
    for item in obj:
        data.append(item)
print(f"data: {data}")

d = [[1, 2, 3], [4, 5, 6], [10, 20, 30]]
for value in chain.from_iterable(d):
    print(value)