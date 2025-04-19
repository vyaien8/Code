class Solution:
    def combinationSum(self, candidates, target):
        res = []
        def bk(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return 
            cur.append(candidates[i])
            bk(i, cur, total + candidates[i]) # continue add condidate[i]
            cur.pop()
            bk(i + 1, cur, total) # no longer use condidate[i]
        
        bk(0, [], 0)
        return res