from math import gcd
from functools import reduce

class Solution:
    def minOperations(self, nums, numsDivide):
        g = reduce(gcd, numsDivide)
        nums.sort()

        for i, x in enumerate(nums):
            if g % x == 0:
                return i

        return -1
