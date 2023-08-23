import operator as op


a = 10
b = 33
result = a + b
print(f"result: {result}")

result = op.add(a, b)    # a + b
print(f"result: {result}")

print(f"op.mul(a, b): {op.mul(a, b)}\n")    #  a * b

colors = ['red', 'purple', 'pink']

print(f"op.getitem(colors, 2): {op.getitem(colors, 2)}\n")   #  colors[2]
