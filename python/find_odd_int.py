"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

# My Answer
def find_it(seq):
    n_repeats = {num:seq.count(num) for num in seq}
    odd_number = []
    for key, val in n_repeats.items():
        if val % 2 == 1:
            odd_number.append(key)
    return odd_number[0]

# Best Answer
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

# Tests Suite
test.describe("Example")
test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)

