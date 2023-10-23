import json
from json import JSONEncoder

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"],
}

# Convert python Dictionary to json string
personJson = json.dumps(person, indent=4, sort_keys=True)
print(f"json as string:\n{personJson}")
# Load
person = json.loads(personJson)
print(f"loaded from json string: {person}")

# Save python Dictionary to json file
with open("json/person.json", "w") as file:
    json.dump(person, file, indent=4, sort_keys=True)
# Load
with open("json/person.json", "r") as file:
    person = json.load(file)
    print(f"loaded from json file: {person}")


# Encoding and decoding classes
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type user is not JSON serializable")


user = User("Max", 27)

# Encode class with default serialize function
userJson = json.dumps(user, default=encode_user)
print(f"Encoded class with default serialize function:\n{userJson}")


# Encode class with custom Encoder class
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return super().default(self, o)


userJson = json.dumps(user, cls=UserEncoder)
print(f"Encoded class with custom Encoder class:\n{userJson}")


# This works but the decoded value will be a dictionary, not a class
user = json.loads(userJson)
print(f"decoded value (bad): {type(user)}")  # dict


# Decode class with default deserialize function
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    raise TypeError("JSON is not deserializable as User")


user = json.loads(userJson, object_hook=decode_user)
print(f"decoded value (good): {type(user)}")  # User
