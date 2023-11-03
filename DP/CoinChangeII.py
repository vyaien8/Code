class Solution:
    def change(self, amount: int, coins: [int]):
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        # dp[i][j] mean number way to get amount i using coins[j:]
        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i+1] # not using coins[i] 
                if a - coins[i] >= 0: # if can using coins[i]
                    dp[a][i] += dp[a-coins[i]][i]
        return dp[amount][0]

    def changeDP(self, amount: int, coins: [int]):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins: # for each coin in coins
            for a in range(1, amount + 1):
                if a - c >= 0: # if can using coin c
                    dp[a] += dp[a - c]
        return dp[amount]
        
test = Solution()
print(test.change(4, [1,1,1,1,1]))
print(test.changeDP(5, [1,2,5]))