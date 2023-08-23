
class Spam(object):
    def __init__(self, value):
        self._value = value

    @property
    def wombat(self):
        return self._value

    def __add__(self, other):
        my_type = type(self)
        return my_type(self._value + other._value)

    def __len__(self):
        return 100
    
    def __str__(self):
        return str(self._value)

class Ham(Spam):
    pass

s1 = Spam(10)
s2 = Spam(20)
s3 = Spam(44)
s4 = Spam(-99)
print(f"s1 + s2: {s1 + s2}")  # "s1 + s2"  same as "s1.__add__(s2)"
print(f"len(s1): {len(s1)}")
print(s1 + s2 + s3)  #  (s1 + s2) + s3     (s1.__add__(s2)).__add__(s3)
print(s1 + s2 + s3 + s4)

print(s1.wombat)

# foo = [1, 2, 3]
# print(dir(foo))

h1 = Ham(100)
h2 = Ham(39)
print(f"h1 + h2: {h1 + h2}")
