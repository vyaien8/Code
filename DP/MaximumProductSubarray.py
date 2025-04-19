class Solution:
    def maxProduct(self, nums: [int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp * n, curMin * n, n)
            res = max(res, curMax)
        return res