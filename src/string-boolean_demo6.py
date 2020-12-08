"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
# def XO(txt):
#     # Your code here
#     txt_lower = txt.lower()
#     return txt.count('x') == txt.count('o')

def XO(txt):
    # lower case our text
    txt_lower = txt.lower()
    x_count = 0
    o_count = 0
    # loop over each character, and count X & O - iterate through
    for char in txt_lower:
        # count how many x's and o's there are
        if char == 'x':
            x_count += 1
        elif char == 'o':
            o_count += 1
    return x_count == o_count


print(XO("ooxx")) # True
print(XO("xooxx")) # False
print(XO("ooxXm")) # True


