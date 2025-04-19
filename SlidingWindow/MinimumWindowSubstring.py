class Solution:
    def minWindow(self, s, t): # find the minimum window of s contain all characters of t
        if len(s) < len(t) or t == "":
            return ""
        dic = {} # character map of t
        window = {}
        for c in t:
            dic[c] = dic.get(c, 0) + 1
        need = len(dic) # number of distince character in s
        have = 0 # number character in window satisfy 
        l = 0
        res = ""
        minlength = len(s) 
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in dic and window[s[r]] == dic[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < minlength:
                    res = s[l: r + 1]
                    minlength = r - l + 1
                window[s[l]] -= 1
                if s[l] in dic and window[s[l]] < dic[s[l]]:
                    have -= 1
                l += 1
        return res