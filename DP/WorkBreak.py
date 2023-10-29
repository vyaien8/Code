class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        dp = {}
        length = len(s)
        dp[length] = True
        for i in range(length - 1, -1, -1):
            dp[i] = False
            for w in wordDict:
                wl = len(w)
                if (i + wl) <= length and s[i: i + wl] == w:
                    dp[i] = dp[i + wl]
                if dp[i]:
                    break
        return dp[0]

