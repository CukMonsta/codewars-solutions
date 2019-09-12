"""
An isogram is a word that has no repeating letters, consecutive or
non-consecutive.

Implement a function that determines whether a string that contains only
letters is an isogram.

Assume the empty string is an isogram, ignore letter case.
"""

def is_isogram(string: str) -> Bool:
    return len(string.lower()) == len(set(string.lower()))


# The best answer to this question is:

def is_isogram(string):
    return len(string) == len(set(string.lower()))
