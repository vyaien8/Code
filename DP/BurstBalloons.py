class Solution:
    def maxCoins(self, nums: [int]):
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            for i in range(l, r + 1): # for each balloon, support it is the last balloon will be bursted
                coin = nums[l - 1] * nums[i] * nums[r + 1]
                coin += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coin)                
        return dfs(1, len(nums) - 2)