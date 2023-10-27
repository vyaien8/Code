class Solution:
    def maxSum(self, nums: [int]):
        dp = {-1: 0}
        res = 0
        for i in range(len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(res, dp[i])
        return res
