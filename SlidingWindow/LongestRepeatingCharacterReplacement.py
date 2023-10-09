class Solution:
    def characterReplacement(self, s, k):
        count = {}
        l = 0
        maxF = 0 # max frequency character
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxF = max(maxF, count[s[r]])
            if (r - l + 1) - maxF > k: # length of window - maxF = number characters that need to replace
                count[s[l]] -= 1
                l += 1
        return (r - l + 1)