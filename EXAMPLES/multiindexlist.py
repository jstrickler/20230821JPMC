

class MultiIndexList(list):  # Define new class that inherits from list

    #  LIST[0]     DICT[KEY]
    #  LIST[0:5]
    #  LIST[1, 5, 9]  does not work in normal list
    #  LIST[1, 5, 9, 19, 2, -1] is shortcut for [LIST[1], LIST[5], LIST[9]]
    def __getitem__(self, index):  # Redefine __getitem__ which implements []
        if hasattr(index, '__iter__'):  # Check to see if index is iterable
            if len(index) == 0:
                raise ValueError("Tuple must be non-empty")
            else:
                tmp_list = []
                for index in index:
                    tmp_list.append(
                        super().__getitem__(index)  # Call list.__getitem__() for each index in tuple
                    )
                return tmp_list
        else:
            return super().__getitem__(index)  # Call the normal __getitem__()


if __name__ == '__main__':
    m = MultiIndexList(
        'banana peach nectarine fig kiwi lemon lime'.split()
    )  # Initialize a MultiIndexList
    m.append('apple')  # Add an element (works like normal list)
    m.append('mango')
    print(m)

    print(f"m[0]: {m[0]}")  # normal indexing
    print(f"m[5, 2, 0]: {m[5, 2, 0]}")  # multi-index with tuple
    print(f"m[:4]: {m[:4]}")  # normal slice
    print(f"len(m): {len(m)}")  # len() works normally
    print(f"m[5,]: {m[5,]}")  # get list with just one item m[5]
    print(f"m[:2,-2:]: {m[:2,-2:]}")  # get list with first two, last two items
    print()
    print(f"m: {m}")
    print(m)
    m.extend(['durian', 'kumquat'])
    print(m)
    print()
    for fruit in m:
        print(fruit)
    print(m[[1, 0, 5]])
