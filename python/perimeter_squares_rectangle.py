"""
The drawing shows 6 squares the sides of which have a lenght of 1,1,2,3,5,8.

It's easy to see that the sum of the perimeters of these squares is:
4 * (1+1+2+3+5+8) = 4 * 20 = 80.

Could you give the sum of the perimeters of all the squares in a rectangle
when there are n+1 squares disposed in the same manner as in the drawing.

# Hint: See Fibonacci sequence
# Ref: http://oeis.org/A000045

The function perimeter has for parameter n where n+1 is the number of squares
(they are numbered from 0 to n) and returns the total parimeter of all the
squares.
"""

# My Answer
def perimeter(n):
    n = n + 1
    count = 3
    fibo_list = [0, 1, 1]
    while count <= n:
        number = fibo_list[-2] + fibo_list[-1]
        fibo_list.append(number)
        count += 1
    return 4 * sum(fibo_list[:])

# Best Answer
def fib(n):
    a, b = 0, 1

    for i in range(n+1):
        if i == 0:
            yield b
        else:
            a, b = b, a+b
            yield b

def perimeter(n):
    return sum(fib(n)) * 4

# Tests Suite
test.assert_equals(perimeter(5), 80)
test.assert_equals(perimeter(7), 216)
test.assert_equals(perimeter(20), 114624)
test.assert_equals(perimeter(30), 14098308)
test.assert_equals(perimeter(100), 6002082144827584333104)
