"""
Challenge #8:

Create a function that returns the number of arguments it was called with.

Examples:
- num_args() ➞ 0
- num_args("foo") ➞ 1
- num_args("foo", "bar") ➞ 2
- num_args(True, False) ➞ 2
- num_args({}) ➞ 1
"""
def num_args(*args, **kwargs):
    # Your code here
    #...array *args  *kwargs = keyword args
    # *args passes variable number of non-keyworded arguments, **kwargs passes variable number of keyword arguments
    print(len(args))
    print(kwargs)
    return

