class Solution:
    def hammingWeight(self, n: int):
        res = 0
        while n:
            res += n % 2
            n >>= 1
        return res