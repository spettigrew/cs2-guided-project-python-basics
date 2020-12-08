"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt):
    # Your code here
    return int(txt)

def int_string(num):
    # Your code here
    return str(num)

# check the type to see if it is a number or string
print(type(string_int("6")))
print(isinstance(string_int("6"), int))

