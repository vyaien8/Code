class Solution:
    # _ _ _ _ _
    #       i
    # dp[i] = i + max(dp[i-2], dp[i-3])
    # because can not rob two adjacent house
    # not include dp[i - 4] or futher because dp[i - 2] always bigger than dp[i - 4] becasue dp[i -2] = nums[i-2] + max(dp[i - 4], dp[i - 5))
    
    def rob(self, nums: [int]) -> int:
        res = 0
        dp = {}
        dp[-3] = 0
        dp[-2] = 0
        dp[-1] = 0
        for i in range(len(nums)):
            dp[i] = nums[i] + max(dp[i-3], dp[i-2])
            res = max(res, dp[i])
        return res
    def rob2(self, nums):
        rob_1, rob_2 = 0, 0
        # [rob_2, rob_1, 0, 1, 2, ...]
        # rob_2: maximum can have in [:i-1]
        # rob_1: maximum can have in [:i]
        for i in nums:
            rob_2, rob_1 = rob_1, max(rob_1, rob_2 + i)
        return rob_1