"""
You like building blocks. You especially like building blocks that are
squares. And what you even like more, is to arrange them into a square
of square building blocks!

However, sometimes, you can't arrange them into a square. Instead,
you end up with an ordinary rectangle!

Those blasted things! If you just had a way to know, whether you're currently
working in vain... Wait!

That's it! You just have to check if your number of building blocks is
a perfect square (search the meaning of perfect square).
"""

# My Answer
def is_square(n):
    if n < 0:
        return False
    else:
        x = n // 2
	y = set([x])
	while x * x != n:
 	    x = (x + (n // x)) // 2
	    if x in y: return False
	    y.add(x)
	return True

# Best Answer
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;
