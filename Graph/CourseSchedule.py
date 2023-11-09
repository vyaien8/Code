class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]):
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True 
test = Solution()
print(test.canFinish(2, [[0, 1]]))