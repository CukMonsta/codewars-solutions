"""
Create a function that returns the sum of the two lowest positive numbers
given an array of minimum 4 positive integers. No floats or non-positive
integers will be passed.
"""

# My Answer
def sum_two_smallest_numbers(numbers):
    my_list = sorted(list(numbers))
    return my_list[0] + my_list[1]

# Best Answer
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
