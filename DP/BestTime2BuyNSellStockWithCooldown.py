class Solution:
    def maxProfit(self, prices: [int]):
        # State: Buy or Sell
        # if buy(True) -> the next index is i + 1
        # if sell(False) -> the next index must be i + 2 because have to take cooldown after sell
        # cannot buy in two continue transaction(buy or sell called a transaction)
        dp = {} # dp[(i, state)] = maxprofit in ith day with state
        def dfs(i, state):
            if i >= len(prices):
                return 0
            if (i, state) in dp:
                return dp[(i, state)]
            cooldown = dfs(i + 1, state) # every state, we always has cooldown as a choice in the next day
            if state: # if we in state can buy
                buy = dfs(i + 1, not state) - prices[i] # if we buy, the profit is the profit of the left day - the price on the ith day
                dp[(i, state)] = max(buy, cooldown)
            else: # if we in state can sell
                dp[(i, state)] = max(dfs(i + 2, not state) + prices[i], cooldown) # if we sell, the next transaction is on i + 2
            return dp[(i, state)]
        return dp[0, True] # the first day, we can buy or cooldown, can not sell
        

