from copy import deepcopy


a = [1, 2, 3]
a.append(4)
print(f"a: {a}")
b = a  # b IS a    'b' is an alias for 'a'    no instantiation (no new object created)
a.append(5)
b.append(6)   # b and a are the same objects
print(f"a: {a}")
print(f"b: {b}")

def spam(items):
    print(f"items: {items}")

spam(a)
spam(b)
spam([8, 9, 10])

c = list(a) # copy of a  (new list, not an alias)
d = a[::]   # copy of a  (also new list)
c.append("wombat")
d.append("apple")
print(f"a: {a}")
print(f"c: {c}")
print(f"d: {d}")




visited = {
    'Bob': ['India', 'Sri Lanka', 'Peru', 'Burkina Faso'],
    'Mary': ['Japan', 'Armenia', 'France', 'Guatemala'],
}

v2 = deepcopy(visited)
visited['Clare'] = ['Sweden', 'Israel', 'Mexico', 'France', 'Lithuania']

print(f"visited: {visited}")
print(f"v2: {v2}")

visited['Mary'].append('Belgium')
visited['Bob'].append("Qatar")
print('-' * 60)

print(f"visited: {visited}")
print(f"v2: {v2}")


# mutable type:
#  list, dict, set 

x = [1, 2, 3], [4, 5, 6]
print(f"type(x): {type(x)}")
x[0].append(99)
print(f"x: {x}")

a = 1, 2, 3
b = (1, 2, 3)
y = tuple(x)
y[0].append("wombat")
print(f"x: {x}")

m = [[1, 5, 99], [8, 5, 47]]  # list of list refs
m1 = m   # alias
m2 = list(m)  # shallow copy
m2[0].append(999)
m3 = deepcopy(m)  # deep copy
m3[0].append(4444)
print(f"m: {m}")
print(f"m2: {m2}")
print(f"m3: {m3}")



