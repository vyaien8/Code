class Solution:
    # accepted
    def groupAnagrams(self, strs):
        ans = {}
        for s in strs:
            count = [0] * 26 # table of alphabet
            for c in s: # map a word into ordered table
                count[ord(c) - ord('a')] += 1 
            count = tuple(count)
            if count in ans: # if the table is already on ans
                ans[count].append(s)
            else:
                ans[count] = []
                ans[count].append(s)
        return ans.values()

    # time limit :))
    def groupAnagrams2(self, strs):
        if len(strs) < 2:
            return strs
        def isAnagram(s , t):
            if len(s) != len(t):
                return False
            dicS, dicT = {}, {}
            
            for i in range(len(s)):
                dicS[s[i]] = 1 + dicS.get(s[i], 0)
                dicT[t[i]] = 1 + dicT.get(t[i], 0)
            return True if dicS == dicT else False
        res = []
        i = 0
        n = len(strs)
        while i < n:
            ana = []
            ana.append(strs[i])
            j = i + 1
            while j < len(strs):
                if isAnagram(strs[i], strs[j]):
                    ana.append(strs[j])
                    strs[j], strs[-1] = strs[-1], strs[j]
                    strs.pop()
                    n -= 1
                else:
                    j += 1
            res.append(ana)
            i += 1
        return res
            
