"""
The goal of this exercise is to convert a string to a new string where each character in the new
string is '(' if that character appears only once in the original string, or ')' if that character
appears more than once in the original string. Ignore capitalization when determining if a character
is a duplicate.

Notes: Assertion messages may be unclear about what they display in some languages. If you read
'...It should encode XXX', the 'XXX' is the expected result, no the input!
"""


# My Answer
def duplicate_encode(word):
    word = word.lower()
    new_word = []
    for char in word:
        if word.count(char) != 1:
            new_word.append(')')
        else:
            new_word.append('(')
    return ''.join(new_word)


# Best Answer
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


# Some Test
Test.assert_equals(duplicate_encode("din"),"(((")
Test.assert_equals(duplicate_encode("recede"),"()()()")
Test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
Test.assert_equals(duplicate_encode("(( @"),"))((")
