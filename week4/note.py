# Data Structures

'''
In the example:

y = [True, False, 5, 5.5, "five"]

False and 5 have a relationship too, they have an order

'''

# Add to a list 'cheaply' with .append()

# abstract: the data structure exists to provide relationships between data, and operations
# on that data.

# concrete: to make a data structure, we need to create operations, and support relationships

## TODO: make a dictionary-style thing, with keys and values
## Rules: you can use classes and listsm but no other data structures



class lookup:
    def __init__(self):
        self.pairs = []


    def _findkeyindex(self, key):
        for index, pair in enumerate(self.pairs):
            k, v = pair
            if k == key:
                return index
        return None

    def set(self, key, value):
        index = self._findkeyindex(key)
        if index is None:
            self.pairs.append([key, value])
        else:
            self.pairs[index][1]

    def get(self, key):
        index = self._findkeyindex(key)
        if index is None:
            raise KeyError(key)
        else:
            return self.pairs[index][1]

    def allkeys(self):
        pass

    def unset(self, key):
        pass

lu = lookup()

lu.set("hi", "mom")
print(lu.get("hi"))
print(lu.get("bye"))