class Solution:
    def characterReplacement(self, s, k):
        count = {}
        res = 0
        l = 0
        maxF = 0 # max frequency character
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxF = max(maxF, count[s[r]])
            while (r - l + 1) - maxF > k: # when the number need to replace is bigger than the maximum allowed
                count[s[l]] -= 1 
                l += 1 
            res = max(res, l - r + 1)
        return res