from collections import namedtuple

person = 'Bill', 'Gates', 'Microsoft'

print(f"person[0]: {person[0]}")
print(f"person[1]: {person[1]}")

Person = namedtuple("Person", "first_name last_name company")

p = Person('Bill', 'Gates', 'Microsoft')
print(f"p[0]: {p[0]}")
print(p.first_name, p.last_name)
print(f"Person: {Person}")
print(f"type(Person): {type(Person)}")
print(f"type(p): {type(p)}")

foo = [1, 2, 3]
print(f"type(foo): {type(foo)}")

print(f"Person.mro(): {Person.mro()}")
