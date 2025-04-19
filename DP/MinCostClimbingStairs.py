class Solution:
    def minCost(self, cost: [int]) -> int:
        # basic idea
        # dp = {}
        # dp[0] = 0
        # dp[1] = 0
        # for i in range(2, len(cost) + 1):
        #     dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        # return dp[len(cost)]
        # better solution
        prev, cur = 0, 0
        for i in range(2, len(cost) + 1):
            prev, cur = cur , min(prev + cost[i - 2], cur + cost[i - 1])
        return cur
    def minCost2(self, cost: [int]):
        # easy understand solution
        # to reach the to any position we have two ways
        # so do it bottom up
        cost.append(0) # from len(cost) position to reach it, took 0
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0],cost[1])
     


test = Solution()
print(test.minCost([10,15,20]))