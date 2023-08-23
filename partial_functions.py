from functools import partial

def doit(func):
    func("blue")


def spam(name, color):
    print(name, color)

s2 = partial(spam, color="purple")

doit(s2)