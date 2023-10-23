# Errors and Exceptions
x = 5

# Raising exceptions
if x < 0:
    raise Exception("x should be positive")

assert x >= 0, "x is not positive"


# Try except blocks
try:
    a = 5 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError " + str(e))
except TypeError as e:
    print("TypeError " + str(e))
except Exception as e:
    print("Unknown error " + str(e))
else:
    print("everything is fine")
finally:
    print("finally clause")


# Define custom errors
class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 0:
        raise ValueTooSmallError("value is too small", x)


try:
    test_value(-1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
