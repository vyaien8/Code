class Solution:
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""
        dic = {} # character map of t
        window = {}
        for i in range(len(t)):
            dic[t[i]] = dic.get(t[i], 0) + 1
            window[s[i]] = window.get(s[i], 0) + 1
        n = len(dic) # number of distince character in s
        k = 0 # number character in window satisfy 
        for i in dic:
            if i in window and dic[i] <= window[i]: # check the first window to find out how many characters already satisfy
                k += 1
        l = 0
        res = ""
        minlength = len(s) 
        for r in range(len(t), len(s)):
            if k == n: # if enough character in window satisfy
                while k == n: # remove all left most character that don't need
                    if s[l] in dic:
                        window[s[l]] -= 1
                        if window[s[l]] < dic[s[l]]:
                            k -= 1
                    l += 1
                if minlength >  (r - l + 1):
                    minlength = r - l + 1
                    res = s[l - 1: r]
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in dic and window[s[r]] == dic[s[r]]:
                k += 1
        if k == n:
            t = len(s)
            while k == n:
                if s[l] in dic:
                    window[s[l]] -= 1
                    if window[s[l]] < dic[s[l]]:
                        k -= 1
                l += 1
            if minlength >= (t - l + 1):
                minlength = t - l + 1
                res = s[l - 1: t]
        return res