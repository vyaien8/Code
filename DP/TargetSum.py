class Solution:
    def findTargetSumWays(self, nums: [int], target: int) -> int:
        dp = {}
        def bk(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = bk(i + 1, total + nums[i]) + bk(i + 1, total - nums[i])
            return dp[(i, total)]
        return bk(0,0)