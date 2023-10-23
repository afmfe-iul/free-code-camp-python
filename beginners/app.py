from math import *
from secrets import randbelow

# Variables

# String
character_name = "John"
# Integer
character_age = 35
# Boolean
isMale = True
# Object
character_object = {"name": character_name, "age": character_age, "isMale": isMale}

print("There once was a man named " + character_object["name"] + ", ")
print("he was " + str(character_age) + " years old. ")
print("He really liked the name " + character_object["name"] + ", ")
print("but didn't like being " + str(character_age) + ".")

print(pow(2, 7))
print(pow(4, 6))

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(len(friends))

# Tuple are immutable
coordinates = (4, 5, 6, 1)

print(coordinates[0])


# Functions
def hello_world(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old.")


hello_world("Andre", 32)


def cube(num):
    return num * num * num


result = cube(4)
print(result)

# If statements
rand_number = randbelow(3)
print("rand_number: " + str(rand_number))

if rand_number < 1:
    print("Less than 1")
elif rand_number < 2:
    print("Less than 2")
else:
    print("Less than 3")


# Try except
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as err:
    print("Invalid input:asd", err)
