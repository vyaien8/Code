class Solution:
    def countBits(self, n):
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = i % 2 + dp[i // 2]
        return dp
test = Solution()
print(test.countBits(8))