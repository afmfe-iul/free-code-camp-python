# lambda arguments : expression

from functools import reduce


add10 = lambda x: x + 10
print(add10(5))


def add10_func(x):
    return x + 10


mult = lambda x, y: x * y
print(mult(2, 7))


# sorting a list of tuples using lambda
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted_by_x = sorted(points2D)  # [(1, 2), (5, -1), (10, 4), (15, 1)]
points2D_sorted_by_y = sorted(
    points2D, key=lambda x: x[1]
)  # [(5, -1), (15, 1), (1, 2), (10, 4)]


# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)  # [2, 4, 6, 8, 10]
print(list(b))

# same as above but with list comprehension
c = [x * 2 for x in a]  # [2, 4, 6, 8, 10]


# filter(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)  # [2, 4, 6]
print(list(b))

# same as above but with list comprehension
c = [x for x in a if x % 2 == 0]  # 2, 4, 6]


# reduce(func, seq)
a = [1, 2, 3, 4, 5, 6]

product_a = reduce(lambda x, y: x * y, a)
print(product_a)
