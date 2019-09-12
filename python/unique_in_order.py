"""
Implement the function which takes as argument a sequence and returns a list
of items without any elements with the same value next to each other and
preserving the original order of elements.
"""

# My Answer
def unique_in_order(iterable):
    newList = []
    for item in iterable:
        if len(newList) < 1 or not item == newList[len(newList) - 1]:
            newList.append(item)
    return newList

# Best Answer
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
