class Solution:
    # does s math the patern p
    def isMath(self, s: str, p: str):
        dp = {}

        def bk(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j > len(p): # when pattern is over but s not
                return False
            # if the current two character is match or pattern is .
            matched = i < len(s) and (s[i] == s[j] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == '*': # if the next char is *
                dp[(i,j)] = (bk(i, j + 2)# if not use *
                or (bk(i + 1, j) and matched)) # if use * (only use the star when the previous is matched)
                return dp[(i,j)]
            if matched: # if next character is not * and the current is match
                dp[(i, j)] = bk(i + 1, j + 1)
                return dp[(i, j)]
            dp[(i, j)] = False
            return False
