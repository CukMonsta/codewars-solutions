"""
You are going to be given an array of integers. Your job is to take that array
and find an index N where the sum of the integers to the left of N is equal
to the sum of the integers of the right of N. If there is no index that would
make this happen, return -1.

For example:

Let's say you are given the array [1, 2, 3, 4, 3, 2, 1]

Your function will return the index 3, because at the 3rd position of the array
the sum of left side of the index [1, 2, 3] and the sum of the right side of
the index [3, 2, 1] both equal 6.

Note: Please remember that in most programming/scripting languages the index of
an array starts at 0.

Note: If you are given an array with mutiple answers, return the lowest correct
index.
"""

# My Answer
def find_even_index(arr):
    result = []
    range_arr = range(0, len(arr))
    for elem in range_arr:
        result.append(sum(arr[:elem]) == sum(arr[elem+1:]))
    if True in result:
        return result.index(True)
    else:
        return -1

# Best Answer
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

# Tests Suite
Test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
Test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
Test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
Test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
Test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
Test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
Test.assert_equals(find_even_index(range(1,100)),-1)
Test.assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
Test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
Test.assert_equals(find_even_index(range(-100,-1)),-1)
