"""
Write a function, 'persistence', that takes in a positive parameter 'num' and
returns its multiplicative persistence, which is the number of times you must
multiply the digits in 'num' until you reach a single digit.

For example:

persistence(39) => 3 Because 3*9 = 27, 2*7 = 14, 1*4 = 4, and 4 has only one digit
"""

# My Answer
import numpy as np

def persistence(n):
    count = 0
    while n > 9:
        n = [int(elem) for elem in str(n)]
        n = np.prod(n)
        count += 1
    return count

# Best Answer
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

# Tests Suite
Test.it("Basic tests")
Test.assert_equals(persistence(39), 3)
Test.assert_equals(persistence(4), 0)
Test.assert_equals(persistence(25), 2)
Test.assert_equals(persistence(999), 4)
