
a = "apple"
b = 123

def spam():
    msg = "I am spam"
    print(f"locals(): {locals()}\n")
    
    print(msg)

g  = globals()
print(f"g: {g}\n")

print(f"g['a']: {g['a']}\n")
g['spam']()

g['color'] = 'blue'  # define a new global variable
print(f"color: {color}\n")

g['bark'] = lambda: print("Woof woof")

bark()
