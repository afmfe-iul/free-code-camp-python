def my_generator():
    yield 1
    yield 2
    yield 3


g = my_generator()

print(next(g))  # 1

for i in g:
    print(i)  # 2 3


# Generators can be passed to functions that take iterators
def reverse_generator():
    yield 3
    yield 2
    yield 1


print(sorted(reverse_generator()))  # [1,2,3]


# Another example
def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)  # This will not print "Starting"

value = next(cd)  # Starting
print(value)  # 4

print(next(cd))  # 3
print(next(cd))  # 2
print(next(cd))  # 1


############ Memory efficiency of generators ############
#########################################################
import sys


def first_n(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def first_n_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(f"first_n(1000000) size: {sys.getsizeof(first_n(1000000))}")
print(f"first_n_generator(1000000) size: {sys.getsizeof(first_n_generator(1000000))}")

print(f"sum(first_n(100)): {sum(first_n(100))}")
print(f"sum(first_n_generator(100)): {sum(first_n_generator(100))}")


########### Fibonacci sequence with Generators ##########
#########################################################
def fibonacci(limit):
    # Next element is the sum of the previous too: 0 1 1 2 3 5 8 13
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
for i in fib:
    print(i)


################## Generator expression #################
#########################################################
my_generator = (i for i in range(10) if i % 2 == 0)
print(f"List from generator: {list(my_generator)}")

# Same as list comprehension
myList = [i for i in range(10) if i % 2 == 0]
print(f"List from list comprehension: {myList}")
