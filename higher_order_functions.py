

def doit(f):
    f()

def hello():
    print("Hello, world")

doit(hello)

fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

fruits_sorted = sorted(fruits, key=str.lower)
print(f"fruits_sorted: {fruits_sorted}\n")

def custom_sort(f):
    return len(f), f.lower()

fruits_sorted = sorted(fruits, key=lambda f: (len(f), f.lower()))
print(f"fruits_sorted: {fruits_sorted}\n")

#  lambda params: (return-value)


airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"sorted(airports.items()): {sorted(airports.items())}\n")

def by_value(item):
    return item[1], item[0]

print(f"sorted(airports.items(), key=by_value): {sorted(airports.items(), key=by_value)}\n")

print(f"sorted(airports.items(), key=lambda a: (a[1], a[0])): {sorted(airports.items(), key=lambda a: (a[1], a[0]))}\n")

data = {
    'foo': [1, 2, 4],
    'bar': [44, 9, 18],
    'blah': [3, 1, 2],
}

print(f"data.items(): {data.items()}\n")

for item in sorted(data.items()):
    print(item)
print()

for item in sorted(data.items(), key=by_value):
    print(item)
print()

def mysort(item):
    return item[1][1]   #  2nd element of value

for item in sorted(data.items(), key=mysort):
    print(item)
print()

