# Tuple: ordered, immutable, allows duplicate elements
myTuple = ("Max",)
myTuple = "Max", 28, "Boston"  # parentheses are optional
print(type(myTuple))

myTuple = tuple(["Max", 28, "Boston"])  # tuple constructor

item = myTuple[0]  # Max

for i in myTuple:
    print(i)  # Max 28 Boston

if "Max" in myTuple:
    print("Max in myTuple")

print(len(myTuple))  # 3

# myTuple.index("nope") # ValueError: tuple.index(x): x not in tuple

myList = list(myTuple)  # convert tuple to list

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(a[0:5:2])  # (1, 3, 5)

#  Unpacking
myTuple = "Max", 28, "Boston"
name, age, city = myTuple

a = (1, 2, 3, 4)
i1, *i2, i3 = a  # i1 = 1, i2 = [2, 3], i3 = 4

# Tuples are faster than lists
import sys
import timeit

myList = [0, 1, 2, "hello", True]
myTuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(myList), "bytes")  # 104 bytes
print(sys.getsizeof(myTuple), "bytes")  # 88 bytes

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))  # 0.026
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))  # 0.009
