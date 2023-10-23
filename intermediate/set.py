# Tuple: unordered, mutable, no duplicated elements
mySet = {1, 2, 3, 4, 5, 5, 5}  # {1, 2, 3, 4, 5}

mySet = set("Hello")  # {'e', 'H', 'l', 'o'} random order, no duplicates

mySet = {}  # this is not a set, it's a dict
mySet = set()  # empty set

mySet.add(1)
mySet.add(2)

mySet.remove(2)  # KeyError if not found
mySet.discard(2)  # no error if not found

mySet.clear()  # empty the set

mySet = {1, 2, 3, 4, 5}

for i in mySet:
    print(i)  # 1 2 3 4 5

if 1 in mySet:
    print("1 in mySet")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# Union
odds.union(evens)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Intersection
odds.intersection(evens)  # set()
odds.intersection(primes)  # {3, 5, 7}

# Difference
odds.difference(primes)  # {1, 9}
primes.difference(odds)  # {2}

odds.symmetric_difference(
    primes
)  # {1, 2, 9} # elements that are in either set, but not in both

# Immutable sets
a = frozenset([1, 2, 3, 4])
