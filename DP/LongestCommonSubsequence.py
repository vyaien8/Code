class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str):
        s1 = '0' + s1
        s2 = '0' + s2
        l1 = len(s1)
        l2 = len(s2)
        dp = [[0] * l2 for i in range(l1)] # dp[i][j]: length of maximum subsequence of s1[:i], s2[:j]
        # base case: dp[i][0] = dp[0][j] = 0
        # dp[i][j] = 1 + dp[i-1][j-1] if s1[i] == s2[j] else max(dp[i-1][j], dp[i][j-1])
        for i in range(1, l1):
            for j in range(1, l2):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[l1-1][l2-1]
test = Solution()
print(test.longestCommonSubsequence("abcde", "ace"))