from carddeck import CardDeck

# instantiate the class
d1 = CardDeck("Amelia")
print(f"d1: {d1}")

d2 = CardDeck("Fergus")

#  obj = ClassName(...)
#  
#  instance = ClassName(args, ...)
d3 = CardDeck()

print(f"d1.dealer_name: {d1.dealer_name}")

# print(d1.get_dealer_name())
# d1.set_dealer_name("Fritz")



# very naughty
# print(f"d2._dealer_name: {d2._dealer_name}")

d1.dealer_name = "Lakmi"
print(f"d1.dealer_name: {d1.dealer_name}")

print(f"d1: {d1}")

x = str(d1)  # CardDeck.__str__(d1)


d1.shuffle()
print(f"d1.cards: {d1.cards}")
for i in range(5):
    print(d1.draw())


