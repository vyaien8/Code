class Solution:
    # brute force
    def longestPalindrome(self, s: str):
        def isPalin(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True
        res = ""
        maxL = 0
        for i in range(len(s)):
            for j in range(0, i - maxL + 1):
                if isPalin(s, j, i):
                    maxL = i - j + 1
                    res = s[j: i + 1]
                    break
        return res 
    # dynamic programing
    # at each position, we find the maximum palindrome can expand from it into both sides
    def DPlongestPalindrome(self, s: str):
        res = ""
        resLen = 0
        n = len(s)
        for i in range(n):
            # odd length
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if (r - l - 1) > resLen:
                resLen = r - l - 1
                res = s[l + 1:r]
            # even length
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if (r - l - 1) > resLen:
                resLen = r - l - 1
                res = s[l + 1: r]
        return res
                        

