"""
In this kata you have to create all permutations of an input string and remove
duplicates, if present. This means, you have to shuffle all letters from the
input in all possible orders.

Examples:
permutations('a'); ['a']
permutations('ab'); ['ab', 'ba']
permutations('aabb'); ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

The order of the permutations doesn't matter.
"""

# My Answer
from itertools import permutations as permu

def permutations(string):
    per_list = [''.join(per) for per in permu(string)]
    return list(dict.fromkeys(per_list))

# Best Answer
import itertools

def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))

# Tests Suite
Test.assert_equals(sorted(permutations('a')), ['a']);
Test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
Test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
