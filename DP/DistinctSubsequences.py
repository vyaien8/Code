class Solution:
    def numDistinct(self, s: str, t: str):
        dp = {}
        def bk(i, j):
            if j >= len(t):
                return 1
            if i >= len(s): # no letter of s left but t still
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if s[i] == t[j]:
                dp[(i,j)] = bk(i + 1, j + 1) + bk(i + 1, j)
            else:
                dp[(i,j)] = bk(i + 1, j)
            return dp[(i,j)]
        return bk(0,0)
test  = Solution()
print(test.numDistinct("drrragon", "dragon"))
        