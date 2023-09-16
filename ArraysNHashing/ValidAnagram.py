class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dicS, dicT = {}, {}
        for i in range(len(s)):
            dicS[s[i]] = 1 + dicS.get(s[i], 0) # get(key, default_value) -> return value of key if key in dic else return default_value
            dicT[t[i]] = 1 + dicT.get(t[i], 0)
        if dicS == dicT:
            return True
        else:
            return False