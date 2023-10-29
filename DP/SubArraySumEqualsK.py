class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        n = len(nums)
        prefix = {0: 1}
        pre = 0
        res = 0
        for i in range(0, n):
            pre += nums[i]
            if (pre - k) in prefix:
                res += prefix[pre - k] 
            prefix[pre] = prefix.get(pre, 0) + 1
        return res

test = Solution()
test.subarraySum([1], 0)           
        

