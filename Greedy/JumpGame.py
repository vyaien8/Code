class Solution:
    # dp solution
    def canJump(self, nums: [int]):
        n = len(nums)
        dp = [False] * (len(nums))
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for j in range(i + 1, i + nums[i] + 1):
                    if j == n - 1:
                        return True
                    if j < len(nums):
                        dp[j] = True                   
        return dp[n - 1]
    # greedy solution
    def canJumpG(self, nums: [int]):
        des = len(nums) - 1
        for i in range(des - 1, -1, -1):
            if nums[i] + i >= des:
                des = i
        return des == 0
test = Solution()
print(test.canJump([2,3,1,1,4]))

