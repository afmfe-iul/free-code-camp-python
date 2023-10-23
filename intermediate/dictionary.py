# Dictionary: Key-value pairs, unordered, mutable
myDict = {"name": "Max", "age": 28, "city": "New York"}
print(myDict)  # {'name': 'Max', 'age': 28, 'city': 'New York'}

# Another way of creating a dictionary
myDict = dict(name="Mary", age=27, city="Boston")

# Accessing items
value = myDict["name"]
print(value)  # Mary

# Adding new item
myDict["email"] = "xyz@gmail.com"

# Removing item
del myDict["email"]
myDict.pop("city")
myDict.popitem()  # removes last inserted item

# Checking if item is in dictionary
if "name" in myDict:
    print(myDict["name"] + " in dic")  # Mary

try:
    print(myDict["lastName"])
except:
    print("Error")

# Looping through dictionary
# myDict.keys() to loop through keys, or myDict.values() for values
for key, value in myDict.items():
    print("Key: " + key + " | Value: " + value)  # Key: name | Value: Max

# Copying dictionary
myDictCopy = myDict.copy()
myDictCopy = dict(myDict)

# Merge two dictionaries
myDictCopy = {"email": "123@gmail.com"}.update(myDict)

# Dictionary keys can be any immutable type: int, float, string, tuple
myDict = {3.14: "pi", "key": "value", (3, 4): [1, 2, 3]}
print(myDict[(3, 4)])  # [1, 2, 3]  # tuple as key
