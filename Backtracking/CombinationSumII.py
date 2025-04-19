class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        candidates.sort()
        res = []
        def bk(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            bk(i + 1, cur, total + candidates[i])
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            bk(i + 1, cur, total)
        bk(0, [], 0)
        return res

test = Solution()
print(test.combinationSum2([2,5,2,1,2], 5))
