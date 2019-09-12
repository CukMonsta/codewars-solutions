"""
Write a method that takes an array of consecutive (increasing) letters
as input and that returns the missing letter in the array.

You will always get and valid array. And it will be always exactly one
letter be missing. The length of the array will always be at least 2.

The array will always contain letters in only one case.

Note: Use the English alphabet with 26 letters.
"""

# My Answer
def find_missing_letter(chars):
    ord_list = [ord(item) for item in chars]
    result = []
    for value in range(1, len(chars)):
        if ord_list[value] - ord_list[value - 1] != 1:
            result.append(chr(ord_list[value] - 1))
    return result[0]

# Best Answer
def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))
