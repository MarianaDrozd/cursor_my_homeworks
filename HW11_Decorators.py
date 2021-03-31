from functools import wraps
# # 1. double_result
# # This decorator function should return the result of another function multiplied by two


def double_result(func):
    def foo(*args):
        return func(*args) * 2
    return foo


def add(a, b):
    return a + b


add(5, 5)
# 10


@double_result
def add(a, b):
    return a + b


print(add(5, 5))
# 20
print(add(-6, 25))
# 38

# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise return the string "Please use only odd numbers!"


def only_odd_parameters(func):
    @wraps(func)
    def odd_num(*args):
        for a in args:
            if a % 2 == 0:
                return "Please use only odd numbers!"
            else:
                return func(*args)
    return odd_num


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5))
# 10
print(add(4, 4))
# "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print(multiply(2, 6, 5, 8, 3))
# Please use only odd numbers!
print(multiply(1, -3, 5, 11, 63))
# -10395

# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):


def logged(funct):
    # log function arguments and its return value
    @wraps(funct)
    def with_logging(*args, **kwargs):
        print(f"you called {funct.__name__}({args}, {kwargs})")
        print(f"it returned {funct(*args, **kwargs)}")
        return funct(*args, **kwargs)

    return with_logging


@logged
def func(*args, **kwargs):
    return 3 + len(args) + len(kwargs)


print(func(4, 4, 4))
# you called func((4, 4, 4), {})
# it returned 6
# 6
print(func(5, 6, 7, x=10, y=-3))
# you called func((5, 6, 7), {'x': 10, 'y': -3})
# it returned 8
# 8

# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.


def type_check(correct_type):
    def check_type(foo):
        def wrapper(x):
            if not isinstance(x, correct_type):
                print(f"Wrong Type: {type(x).__name__}")
            else:
                return foo(x)
        return wrapper
    return check_type


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
# 4
print(times2('Not A Number'))  # "Wrong Type: string" should be printed, since non-int passed to decorated function
# Wrong Type: str
# None

@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
# H
print(first_letter(['Not', 'A', 'String']))  # "Wrong Type: list" should be printed, since non-str passed to decorated
# function

# Wrong Type: list
# None
