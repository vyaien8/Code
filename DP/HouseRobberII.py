class Solution:
    def rob(self, nums: [int]) -> int:
        def srob(a):
            res = 0
            dp = {}
            dp[-3] = 0
            dp[-2] = 0
            dp[-1] = 0
            for i in range(len(a)):
                dp[i] = a[i] + max(dp[i-2], dp[i-3])
                res = max(res, dp[i])
            return res
        if len(nums) == 1:
            return nums[0]
        return max(srob(nums[1:]), srob(nums[:-1]))
    
