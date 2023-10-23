import secrets
import numpy as np

a = secrets.randbelow(10)  # real random number [0,10[
print(a)

a = secrets.randbits(4)  # real random bits of size N: 0000 to 1111 in this case
print(a)

myList = list("ABCDEFGH")
a = secrets.choice(myList)
print(a)

# Numpy examples

# Random Floats
a = np.random.rand()
print(f"Random float: {a}")
floatList = np.random.rand(3)
print(f"List: {floatList}")
floatArray = np.random.rand(3, 3)
print(f"Array: {floatArray}")

# Random integers
a = np.random.randint(0, 10)
print(f"Random integer: {a}")
intList = np.random.randint(0, 10, 3)
print(f"List: {intList}")
intArray = np.random.randint(0, 10, (3, 3))
print(f"Array: {intArray}")
