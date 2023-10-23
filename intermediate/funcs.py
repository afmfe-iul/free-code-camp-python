def print_name(name):  # name is the parameter
    print("print_name", name)


print("Andre")  # Andre is the argument


def foo(a, b, c, d=4):  # 'd' is a default argument, must be at the end
    print("foo", a, b, c, d)


foo(1, 2, 3)  # positional arguments
foo(c=1, b=2, a=3)  # keyword arguments
# foo(1,b=2,3) raises an error because we can't use positional args after keyword args
# foo(1,b=2, a=3) raises an error because same arg is repeated


# accepts variable number of args and of keyword args
def bar(a, b, *args, **kwargs):
    print(
        "bar",
        a,
        b,
    )
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


bar(1, 2, 3, 4, 5, six=6, seven=7)


def force_kwargs(*, a, b, c):
    print("force_kwargs", a, b, c)


force_kwargs(a=1, b=2, c=3)


# Unpack args (length of container must match # parameters, and for dicts the keys must match the parameter names)
def unpack_test(a, b, c):
    print("unpack_test", a, b, c)


myList = [1, 2, 3]
unpack_test(*myList)
myList = (1, 2, 3)
unpack_test(*myList)
myDict = {"a": 1, "b": 2, "c": 3}
unpack_test(*myDict)  # unpack_test a b c
unpack_test(**myDict)  # unpack_test 1 2 3


number = 0


def local_var_test():
    number = 3
    print("local_var_test", number)


local_var_test()
print("global number", number)


def global_var_test():
    global number
    number = 3


global_var_test()
print("global number", number)
