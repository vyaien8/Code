class Solution:
    def findOrder(self, courseNums: int, prerequisites: [[int]]):
        preMap = {i:[] for i in range(courseNums)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        res = []
        visit = set()
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.add(crs)
            cycle.remove(crs)
            res.append(crs)
            return True
        for c in range(courseNums):
            if not dfs(c):
                return []
        return res
