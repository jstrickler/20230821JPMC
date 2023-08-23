from datetime import datetime
import logging
from functools import wraps

logging.basicConfig(filename="deco.log", level=logging.INFO)


def timestamp(func):
    @wraps(func)
    def replacement(*args, **kwargs):
        logging.info("Function %s called at %s", func.__name__, datetime.now().ctime())
        result = func(*args, **kwargs)
        return result
        
    return replacement

@timestamp
def spam():
    print("SPAM SPAM SPAM")
    return 100

#spam = timestamp(spam)

print(f"spam: {spam}")
x = spam()
print(f"x: {x}")

@timestamp
def ham(color):
    print("ham ham hammy", color)

ham("blue")
ham("green")

print(ham.__name__, spam.__name__)