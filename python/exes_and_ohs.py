"""
Check to see if a string has the same amount of 'x' and 'o'.
The method must return a boolean and be case insensitive. 
The string can contain any char.
"""

# My Answer
def xo(s):
    count_x = s.lower().count('x')
    count_o = s.lower().count('o')
    if count_x == count_o:
        return True
    else:
        return False

# Best Answer
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

