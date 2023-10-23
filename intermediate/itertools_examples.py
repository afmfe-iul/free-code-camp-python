# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import (
    product,
    permutations,
    combinations,
    combinations_with_replacement,
    accumulate,
    groupby,
    count,
    cycle,
    repeat,
)
import operator


# product: cartesian product of input iterables
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))  # [(1, 3), (1, 4), (2, 3), (2, 4)]

# permutations: all possible orderings, no repeated elements
a = [1, 2, 3]
perm = permutations(a)  # 3! = 6 permutations
print(list(perm))  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
perm = permutations(a, 2)  # 3P2 = 6 permutations
print(list(perm))  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


# combinations: all possible orderings, no repeated elements, order doesn't matter
a = [1, 2, 3, 4]
comb = combinations(a, 2)  # 4C2 = 6 combinations
print(list(comb))  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

comb_wr = combinations_with_replacement(a, 2)  # 4C2 + 4 = 10 combinations
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
print(list(comb_wr))


# accumulate: returns accumulated sums or accumulated results of other binary functions
a = [1, 2, 3, 4]
acc = accumulate(a)  # by default returns accumulated sums
print(a)  # [1, 2, 3, 4]
print(list(acc))  # [1, 3, 6, 10]

acc = accumulate(a, operator.mul)  # returns accumulated results of multiplication
print(a)  # [1, 2, 3, 4]
print(list(acc))  # [1, 2, 6, 24]


# groupby: groups values based on a function
a = [1, 2, 3, 4]
groupObj = groupby(a, key=lambda x: x < 3)

for key, value in groupObj:
    print(key, list(value))  # True [1, 2] \n False [3, 4]


# count: infinite iterator
for i in count(10):  # starts at 10
    print(i)
    if i == 15:
        break


# cycle: infinite iterator
a = [1, 2, 3]
cyclesCount = 1
for i in cycle(a):
    print(i)  # 1, 2, 3, 1, 2, 3
    if i == a[-1]:
        if cyclesCount == 2:
            break
        cyclesCount += 1

# repeat: infinite iterator
for i in repeat(1, 4):  # 1, 1, 1, 1
    print(i)
