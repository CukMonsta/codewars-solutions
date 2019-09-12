"""
Write a function that takes a string of braces, and determines if the order of
the braces is valid. It should return 'True' if the string is valid, and
'False' if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new
characters: brackets [] and curly braces {}

All input strings will be nonempty and will only consist of parentheses,
brackets and curly braces: ()[]{}.

What is considered Valid?

A string of braces is considered valid if all braces are matched with the
correct brace.

Examples:

(){}[] => True
([{}]) => True
(}     => False
[(])   => True
"""

# My Answer
def validBraces(string):
    parenthesis = []
    pardict = {"{":"}", "[":"]", "(":")", "}":"{", "]":"[", ")":"("}
    for i in range(len(string)):
        if string[i] == "(" or string[i] == "[" or string[i] == "{":
            parenthesis.append(string[i])
        else:
            if len(parenthesis) == 0:
                return False
            elif pardict[string[i]] == parenthesis[len(parenthesis)-1]:
                del parenthesis[len(parenthesis)-1]
            else:
                return False
    if len(parenthesis) != 0:
        return False
    return True

# Best Answer
def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0

# Tests Suite
test.expect(validBraces( "()" ), True);
test.expect(not validBraces( "[(])" ), False);
