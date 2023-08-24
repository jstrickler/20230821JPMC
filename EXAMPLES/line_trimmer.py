def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')  # 'yield' causes this function to return a generator object

mary_in = trimmed('../DATA/mary.txt')
for trimmed_line in mary_in:
    print(trimmed_line)
print(f"type(mary_in): {type(mary_in)}")
print(f"hasattr(mary_in,'__iter__'): {hasattr(mary_in,'__iter__')}")
print(f"hasattr(mary_in, '__next__'): {hasattr(mary_in, '__next__')}")
