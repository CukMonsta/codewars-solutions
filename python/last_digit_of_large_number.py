"""
Define a function that takes in two non-negative intergers a and b and
returns the last decimal digit of a**b. Note that a and b may be very large.

For example, the last decimal digit of 9**7 is 9, since 9**7 = 4782969.
The last decimal digit of (2**200)**(2**300), which has over 10**92 decimal
digits, is 6. Also, please take 0**0 to be 1.

You may assume that the input will always be valid.
"""

# My Answer
def last_digit(n1, n2):
    return pow(n1, n2, 10)

# Best Answer
def last_digit(n1, n2):
    return pow( n1, n2, 10 )

# Tests Suite
Test.it("Example tests")
Test.assert_equals(last_digit(4, 1), 4)
Test.assert_equals(last_digit(4, 2), 6)
Test.assert_equals(last_digit(9, 7), 9)
Test.assert_equals(last_digit(10, 10 ** 10), 0)
Test.assert_equals(last_digit(2 ** 200, 2 ** 300), 6)
Test.assert_equals(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)

Test.it("x ** 0")
for nmbr in range(1, 9):
    a = nmbr ** nmbr
    Test.it("Testing %d and %d" % (a, 0))
    Test.assert_equals(last_digit(a, 0), 1, "x ** 0 must return 1")
