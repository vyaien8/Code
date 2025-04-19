class Solution:
    # top down
    def minimumPath(self, grid: [[int]]):
        ROW = len(grid)
        COL = len(grid[0])
        dp = [[float("inf")] * (COL + 1) for i in range(ROW + 1)]
        dp[0][1] = 0
        for i in range(1, ROW + 1):
            for j in range(1, COL + 1):
                dp[i][j] = grid[i - 1][j - 1] + min(dp[i][j - 1], dp[i - 1][j])
        return dp[ROW][COL]
test = Solution()
print(test.minimumPath([[1,3,1], [1,5,1], [4,2,1]]))