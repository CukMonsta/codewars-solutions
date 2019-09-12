"""
Take 2 strings s1 and s2, including only letters from a to z. Return
a new sorted string, the longest possible, containing distinct letters.

Each taken only once - coming from s1 or s2.
"""

def longest(s1, s2):
    string1 = ''.join(set(s1))
    string2 = ''.join(set(s2))
    string = string1 + string2
    return ''.join(sorted((set(string))))

# Best Answer

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))
