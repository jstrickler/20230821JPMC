from pyparsing import *

'''
    inifile ::= section+
    section ::= section_tag + section_data
    section_tag ::= '[' alphanums+ ']'
    section_data ::= key_value_pair+
    key_value_pair ::= key '=' value
    key ::= alphanums+
    value ::= chars+
'''

value = Word(' \t' + printables, excludeChars='=')('value')  # A value can be any character, plus space or tab, _except_ '='
key = Word(alphanums)('key')  # A key can be any alphanumeric character (but not '=')
key_value_pair = Group(key + Suppress('=') + value)  # A key/value pair is key + '=' + value
section_data = Group(OneOrMore(key_value_pair))('keylist')  # Section data is one or more key/value pairs
start_tag = Suppress('[')   # Section start tag is '['
end_tag = Suppress(']')   # Section end tag is ']'
section_tag = start_tag + Word(alphanums)('section') + end_tag  # Section tag is start tag + alphanumerics + end tag
section = Group(section_tag + section_data + Suppress(Optional(White())))  # Section is section tag + section data
ini_file = OneOrMore(section)  # Complete file is one or more sections

with open('../DATA/application.ini') as ini_in:
    contents = ini_in.read()  # Read contents into a string

for section in ini_file.parseString(contents):  # Parse the string
    print(section.section)  # Grab the section name
    for key, value in section.keylist:   # Iterate over key/value pairs in that section
        print('\t{:10s} {}'.format(key, value))
