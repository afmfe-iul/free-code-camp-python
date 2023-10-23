# Strings: ordered, immutable, text representation

# Multiline strings
myString = """Hello
World"""

if "ell" in myString:
    print("ell in myString")

myString = myString.strip()  # remove whitespace

myList = ["a"] * 1000000

myString = "".join(myList)  # faster than concatenation

# Formatting
name = "Tom"
age = 25
height = 1.8

myString = "%s is %d old and %.2f meters tall" % (name, age, height)
print(myString)

myString = "{} is {} old and {:.2f} meters tall".format(name, age, height)
print(myString)

# f-Strings (Python 3.6+) fastest method
myString = f"{name} is {age} old and {height:.2f} meters tall"
print(myString)
