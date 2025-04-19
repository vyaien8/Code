class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        curSum = 0
        res = nums[0]
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            res = max(res, curSum)
        return res
