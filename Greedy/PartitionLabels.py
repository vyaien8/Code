class Solution:
    def partitionLabels(self, s: str):
        last = {}
        n = len(s)
        for i in range(n):
            last[s[i]] = i
        l, r = 0, 0
        res = []
        while r < n:
            r = last[s[l]]
            i = l + 1
            while i < r and r != n - 1:
                r = max(r, last[s[i]])
                i += 1
            res.append(r - l + 1)
            r += 1
            l = r
        return res
test = Solution()
print(test.partitionLabels("ababcbacadefegdehijhklij"))
