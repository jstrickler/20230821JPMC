import inspect
import geometry
from carddeck import CardDeck

deck = CardDeck("Leonard")

things = (
    geometry,  # module
    geometry.circle_area,  # function
    CardDeck,   # class
    CardDeck.get_ranks,   # class method
    deck,   # class instance
    deck.shuffle,   # instance method
)

print("Name               Module?  Function?  Class?  Method?")
for thing in things:
    try:
        thing_name = thing.__name__
    except AttributeError:
        thing_name = type(thing).__name__ + " instance"
    print("{:18s} {!s:6s}   {!s:6s}     {!s:6s}  {!s:6s}".format(
        thing_name,
        inspect.ismodule(thing),  # test for module
        inspect.isfunction(thing),  # test for function
        inspect.isclass(thing),  # test for class
        inspect.ismethod(thing),
    ))


print()
def spam(p0, /, p1, p2='a', *p3, p4, p5='b', **p6):  # define a function
    print(p1, p2, p3, p4, p5, p6)

spam(100, p4=200)

def toast(foo, bar):
    print(foo, bar)

toast(5, 10)
toast(bar=8, foo=99)


# get argument specifications for a function
print("Function spec for Ham:", inspect.getfullargspec(spam))
print()

def bloop(*args, **kwargs):
    pass

# get frame (function call stack) info
print("Current frame:", inspect.getframeinfo(inspect.currentframe()))
