import random

a = random.random()  # float
print(a)
a = random.uniform(1, 5)  # float
print(a)

a = random.randint(1, 10)  # range [1,10]
print(a)

a = random.randrange(1, 10)  # range [1,10[
print(a)

# Pick random element
myList = list("ABCDEFGH")
a = random.choice(myList)
print(a)

# Pick random elements (duplicates possible)
a = random.choices(myList, k=3)
print(a)

# Pick random elements (no duplicates)
a = random.sample(myList, 3)
print(a)

# Shuffle list in place
random.shuffle(myList)
print(myList)
myList.sort()

# These are pseudo randoms because re-seeding will generate the same random numbers again
random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))
