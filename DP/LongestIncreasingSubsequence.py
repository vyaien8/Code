class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        # find the first bigger or equal target
        def upper_bound(target, arr: [int]):
            l, r = 0, len(arr) - 1
            res = -1
            while l <= r:
                m = (l + r) // 2
                if arr[m] >= target:
                    res = m
                    r = m - 1
                else:
                    l = m + 1
            return res
            
        dp = [float("inf")] * (len(nums) + 2)
        dp[0] = float("-inf")
        res = 0
        for i in range(len(nums)):
            index = upper_bound(nums[i], dp)
            dp[index] = nums[i]
            res = max(res, index)
        return res
test = Solution()
print(test.lengthOfLIS([10,9,2,5,3,7,101,18]))