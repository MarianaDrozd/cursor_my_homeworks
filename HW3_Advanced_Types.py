import functools as f

# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

# my output:
# 9786592
# 140606118756912
# 140606118750240
# 140606119659456
# 140606119617024

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))

# my output:
# 139873134483392

# 3. Define the type of each object from step 1.
print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

# my output:
# <class 'int'>
# <class 'str'>
# <class 'set'>
# <class 'list'>
# <class 'dict'>

# 4*. Check the type of the objects by using isinstance.

print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

# my output:
# True
# True
# True
# True
# True

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}.

print("Anna has {} apples and {} peaches.".format(3, 6))

# my output:
# Anna has 3 apples and 6 peaches.

# 6. By passing index numbers into the curly braces.

print("Anna has {1} apples and {0} peaches.".format(3, 6))

# my output:
# Anna has 6 apples and 3 peaches.

# 7. By using keyword arguments into the curly braces.

print("Anna has {apples} apples and {peaches} peaches.".format(apples=5, peaches=10))

# my output:
# Anna has 5 apples and 10 peaches.

# 8*. With indicators of field size (5 chars for the first and 3 for the second)

print("Anna has {0:5} apples and {1:3} peaches.".format(7, 2))

# my output:
# Anna has     7 apples and   2 peaches.

# 9. With f-strings and variables

apples = 2
peaches = 9
print(f"Anna has {apples} apples and {peaches} peaches.")

# my output:
# Anna has 2 apples and 9 peaches.

# 10. With % operator

print("Anna has %s apples and %s peaches." % (apples, peaches))

# my output:
# Anna has 2 apples and 9 peaches.

# 11*. With variable substitutions by name (hint: by using dict)

my_dict = {"apples": apples, "peaches": peaches}
print("Anna has %(apples)s apples and %(peaches)s peaches." % my_dict)

# my output:
# Anna has 2 apples and 9 peaches.

# Comprehensions:
# (1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)



# (2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]


# 12. Convert (1) to list comprehension


lst_comp = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]


print(lst_comp)
# output in the test:
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]
# my output:
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]


# 13. Convert (2) to regular for with if-else


lst_comprehension = []
for num in range(10):
    if num % 2 == 0:
        lst_comprehension.append(num // 2)
    else:
        lst_comprehension.append(num * 10)

print(list_comprehension)
# output in the test:
# [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

print(lst_comprehension)
# my output:
# [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]



# (3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)


# (4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)


# (5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}

# (6)
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}

# 14. Convert (3) to dict comprehension.

d_comprehension = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d_comprehension)
# output in the test:
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# my output:
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# 15*. Convert (4) to dict comprehension.

d_comprehension1 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d_comprehension1)

# output in the test:
# {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}
# my output:
# {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

# 16. Convert (5) to regular for with if.

dict_comprehension_r = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension_r[x] = x ** 3
print(dict_comprehension_r)

# output in the test:
# {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}
# my output:
# {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

# 17*. Convert (6) to regular for with if-else.

dict_comprehension2 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension2[x] = x ** 3
    else:
        dict_comprehension2[x] = x
print(dict_comprehension2)

# output in the test:
# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}
# my output:
# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}


# Lambda:

# (7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y

# (8)
foo = lambda x, y, z: z if y < x and x > z else y

# 18. Convert (7) to lambda function
func = lambda x, y: x if x < y else y
print(func(2, 6))
# output in the test:
# 2
# my output:
# 2

# 19*. Convert (8) to regular function

def foo2(x, y, z):
    if y < x:
        return z
    elif x > z:
        return z
    else:
        return y
print(foo2(1, 2, 3))

# output in the test:
# 2
# my output:
# 2

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max

print(sorted(lst_to_sort))

# my output:
# [1, 5, 13, 15, 18, 24, 33, 55]

# 21. Sort lst_to_sort from max to min

print(sorted(lst_to_sort, reverse=True))

# my output:
# [55, 33, 24, 18, 15, 13, 5, 1]

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2

print(list(map(lambda i: i * 2, lst_to_sort)))

# my output:
# [10, 36, 2, 48, 66, 30, 26, 110]

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]

list_C = list(map(lambda a, b: a ** b, list_A, list_B))
print(list_C)

# my output:
# [32, 729, 16384]

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
print(f.reduce(lambda x, y: x + y, lst_to_sort))

# my output:
# 164

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

print(list(filter(lambda elem: elem % 2 == 1, lst_to_sort )))

# my output:
# [5, 1, 33, 15, 13, 55]

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
print(list(filter(lambda b: b < 0, b)))

# my output:
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]

print(list(filter(lambda value: value in list_2, list_1)))

# my output:
# [2, 3, 5, 7]
