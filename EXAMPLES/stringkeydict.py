

class StringKeyDict(dict):  # Create class that inherits from dict
    def __setitem__(self, key, value):  # Overwrite how values are stored in the dict via _DICT_[_KEY_] = _VALUE_
        if isinstance(key, str):   # Make sure key is a string
            super().__setitem__(key, value)  # Use dict's setitem to set value if it is not a key
        else:
            raise TypeError("Keys must be strings not {}s".format(  # Raise error if non-string key is used
                type(key).__name__
            ))


if __name__ == '__main__':
    d = StringKeyDict(a=10, b=20)   # Create and initialize StringKeyDict instance
    for k, v in [('c', 30), ('m', 'mongoose'), ('d', 40), (1, 50), (('a', 1), 60), (5.6, 201), (['a', 'b'], ['c', 'd'])]:
        try:
            print("Setting {} to {}".format(k, v), end=' ')
            d[k] = v   # Try to add various key/value pairs   d.__setitem__(k, v)
        except TypeError as err:
            print(err)  # Error raised on non-string key
        else:
            print('SUCCESS')

    print()
    print(d)
