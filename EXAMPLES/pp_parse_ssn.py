from pyparsing import *

'''  # Topdown reference grammar
grammar:
ssn = nums+ dash nums+ dash nums+
dash = '-'
nums = '0' | '1' | '2' etc etc
'''

dash = Suppress('-')  # Define dash for readability

ssn_parser = Combine(
    Word(nums, exact=3)  # Match exactly 3 digits
    + dash
    + Word(nums, exact=2)
    + dash
    + Word(nums, exact=4)
)   # Parser combines numbers and dashes
ssn_parser('ssn')
ssn_parser.setName("ssn")

input_string = """
    xxx 215-72-8314 yyy
    102-46-6919 zzz 182-19-2201
"""

for matches, start, stop in ssn_parser.scanString(input_string):
    print(matches, start, stop)


