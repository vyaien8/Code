class Solution:
    def coinChange(self, coins: [int], amount: int):
        dp = {0: 0} # dp[i] is the least number coint need to sum up to i
        for i in range(1, amount + 1):
            dp[i] = float("inf")
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != float("inf") else -1
    
    

