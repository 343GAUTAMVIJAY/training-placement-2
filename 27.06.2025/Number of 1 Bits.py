class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        while n:
            if n & 1:
                sum += 1
            n = n >> 1
        return sum
