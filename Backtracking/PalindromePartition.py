class Solution:
    def isParlin(self,s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def partition(self, s: str):
        res = []
        cur = []
        def bk(i):
            if i >= len(s):
                res.append(cur[:])
                return
            for j in range(i, len(s)):
                if self.isParlin(s,i,j):
                    cur.append(s[i: j + 1])
                    bk(j + 1)
                    cur.pop()
        bk(0)
        return res
test = Solution()
test.partition("aab")