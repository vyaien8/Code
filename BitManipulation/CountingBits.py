class Solution:
    def countBits(self, n: int):
        dp = 0 * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i % 2 + dp[i // 2]
        return dp