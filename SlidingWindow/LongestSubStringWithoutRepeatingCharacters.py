class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        res = 1
        dic = {} # save the last index of s[i]
        l, r = 0, 1
        dic[s[l]] = l
        while r < len(s):
            if s[r] in dic: # if has duplicate
                i = dic.get(s[r]) # get index of duplicate
                dic.pop(s[r])
                if l <= i: # if the repeating character in range [l, r]
                    l = i + 1
            res = max(res, r - l + 1)
            dic[s[r]] = r
            r += 1
        return res