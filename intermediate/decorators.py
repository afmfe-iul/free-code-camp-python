from doctest import debug
import functools


################## Most basic decorator #################
#########################################################


def start_end_decorator(func):
    @functools.wraps(func)  # Tells python about the identity of this function
    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


# The code below is equal to:
# def print_name():
#     print("Andre")
# print_name = start_end_decorator(print_name)
@start_end_decorator
def print_name():
    print("Andre")


print_name()


###### Decorator for function with args and return ######
#########################################################


def start_end_decorator_with_args_and_return(func):
    @functools.wraps(func)  # Tells python about the identity of this function
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper


@start_end_decorator_with_args_and_return
def add5(x):
    return x + 5


print(add5(10))


############### Decorator that takes args ###############
#########################################################


def repeat(times):
    def decorator_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_func


@repeat(times=3)
def greet(name):
    print(f"Hello {name}")


greet("Andre")

################### Nested Decorators ###################
#########################################################


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # !r == repr()
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result

    return wrapper


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper


@debug
@start_end_decorator
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting


say_hello("Andre")


################### Class Decorators ####################
#########################################################

# Used when we want to maintain and update state


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello(name):
    print(f"Hello {name}")


say_hello("Andre")
say_hello("Andre")
