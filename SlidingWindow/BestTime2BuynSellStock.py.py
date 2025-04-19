class Solution:
    def maxProfit(self, prices):
        minP = prices[0]
        res = 0
        for i in prices[1:]:
            if minP > i:
                minP = i
                continue
            else:
                res = max(res, i - minP)
        return res