class Solution(object):
    def twoSum(self, a, sum):
        # using dictionary
        preDic = {}
        for i, v in enumerate(a):
            diff = sum - v
            if diff in preDic:
                return [preDic[diff], i]
            preDic[v] = i 

    def twoSum2(self, a, sum):
        # using two pointer
        s = sorted(a)
        i, j = 0, len(a) - 1
        while i < j:
            if s[i] + s[j] == sum:
                b = a.index(s[i])
                if s[i] == s[j]:
                    e = a.index(s[j], b + 1)
                else:
                    e = a.index(s[j])
                return [b, e] if b < e else [e, b]
            elif s[i] + s[j] > sum:
                j -= 1
            else:
                i += 1
        