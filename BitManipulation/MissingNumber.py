class Solution:
    def missingNumber(self, nums: [int]):
        res = 0
        for i in range(len(nums) + 1):
            res ^= i
        for i in nums:
            res ^= i
        return res