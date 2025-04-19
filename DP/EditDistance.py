class Solution:
    def editDistance(self, s1: str, s2: str):
        dp = [[float("inf")] *(len(s2) + 1) for i in range(len(s1) + 1)]
        # dp[i][j] the minimum change to make s1[i:] = s2[j:]
        # base case
        # dp[len(s1)][j] = len(s2) - j: in this case s1 is null
        # dp[i][len(s2)] = len(s1) - i: in this case s2 is null
        for j in range(len(s2) + 1):
            dp[len(s1)][j] = len(s2) - j
        for i in range(len(s1) + 1):
            dp[i][len(s2)] = len(s1) - i
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1+ min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
                    # using delete character -> (i + 1, j)
                    # using insert character -> (i, j + 1)
                    # using replace -> (i + 1, j + 1)
        return dp[0][0]
