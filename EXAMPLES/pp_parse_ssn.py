from pyparsing import *

'''  # Topdown reference grammar
grammar:
ssn = nums+ dash nums+ dash nums+
dash = '-'
'''

dash = Suppress('-')  # Define dash for readability
dash = '-'  # Define dash for readability

ssn_parser =    Combine(Word(nums, exact=3)  # Match exactly 3 digits
    + dash
    + Word(nums, exact=2)
    + dash
    + Word(nums, exact=4)
   # Parser combines numbers and dashes
)
ssn_parser('ssn')
ssn_parser.setName("ssn")

input_string = """
    xxx 215-72-8314 yyy
    102-46-6919 zzz 182-19-2201
"""

#  [(matches, start, stop), (matches, start, stop), (matches, start, stop), ...]
for result in ssn_parser.scanString(input_string):
    print(result)
print('-' * 60)
for result in ssn_parser.searchString(input_string):
    print(result)
print('-' * 60)
input_string = "231-93-7402abc xyz junk stuff spam"
for result in ssn_parser.parseString(input_string):
    print(result)


