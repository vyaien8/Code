from collections import deque
class Solution:
    def orangesRotting(self, grid:[[int]]):
        rotten = deque()
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c, 0))
        res = 0
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while rotten:
            row, col, res = rotten.popleft()
            for dr, dc in d:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                    grid[r][c] = 2
                    rotten.append((r, c, res + 1))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return res

