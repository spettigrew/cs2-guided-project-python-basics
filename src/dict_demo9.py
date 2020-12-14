"""
Challenge #9:

Write a function that creates a dictionary with each (key, value) pair being
the (lower case, upper case) versions of a letter, respectively.

Examples:
- mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
- mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
- mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

Notes:
- All of the letters in the input list will always be lowercase.
"""
def mapping(letters):
    # Your code here
    # dict, hashmap, hashtable, object = (key, value) data structure.
    letter_dict = {}        # {} sets it to a dict, [] sets it to an array.
    for letter in letters:
        # add a new key/value to the dict.
        # the key is the letter - create a new key
        letter_dict[letter] = letter.upper()
        #    key ^              value^
        # Value is the Capitalized version of the letter

    return letter_dict