class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = {}
        for c in s1:
            dic1[c] = dic1.get(c, 0) + 1
        l, r = 0, 0
        dic2 = {}
        while r < len(s2):
            dic2[s2[r]] = dic2.get(s2[r], 0) + 1
            if s2[r] not in dic1: # if rightmost window not in s1
                l = r + 1
                dic2 = {}
            else:
                while dic2[s2[r]] > dic1[s2[r]]: # while number of a character in window more than the one on s1
                    dic2[s2[l]] -= 1
                    if dic2[s2[l]] == 0:
                        dic2.pop(s2[l])
                    l += 1
            if dic2 == dic1:
                return True
            r += 1
        return False
    
    def checkInclude(self, s1: str, s2: str):
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        dic1, dic2 = {}, {}
        for i in range(l1):
            dic1[s1[i]] = dic1.get(s1[i], 0) + 1
            dic2[s2[i]] = dic2.get(s2[i], 0) + 1
        if dic1 == dic2:
            return True
        l = 0
        for r in range(l1, l2):
            dic2[s2[l]] -= 1
            if dic2[s2[l]] == 0:
                dic2.pop(s2[l])
            l += 1
            dic2[s2[r]] = dic2.get(s2[r], 0) + 1
            if dic1 == dic2:
                return True
        return False
    
test = Solution()
print(test.checkInclude("ab", "edibaooo"))

