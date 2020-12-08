"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def sort_by_length(lst):
    # Your code here
    # the lambda method returns the item without needing to do a return statement
    # lst.sort(key = lambda list_item: len(list_item))
    # lst.sort(key = len, reverse=True) return largest to smallest order (reversed)
    lst.sort(key = len)
    print(lst)

sort_by_length(["apple", "pie", "shortcake"])
