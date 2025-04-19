class Solution:
    def singleNumber(self, nums: [int]):
        res = 0
        for i in nums:
            res ^= i
        return res
    