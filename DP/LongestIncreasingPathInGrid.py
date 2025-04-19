class Solution:
    def longestPath(self, matrix: [[int]]):
        ROW = len(matrix)
        COL = len(matrix[0])
        dp = {}
        def dfs(i, j, prev):
            if i < 0 or i >= ROW or j < 0 or j >= COL or matrix[i][j] <= prev:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1
            res = max(res, 1 + dfs(i + 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i - 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i, j + 1, matrix[i][j]))
            res = max(res, 1 + dfs(i, j - 1, matrix[i][j]))
            dp[(i,j)] = res
            return res
        for i in range(ROW):
            for j in range(COL):
                dfs(i,j,-1)
        return max(dp.values())
test = Solution()
print(test.longestPath([[9,9,4], [6,6,8], [2,1,1]]))
# 9 9 4
# 6 6 8
# 2 1 1

        