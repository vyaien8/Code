from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: [[int]]):
        if not grid:
            return 0
        res = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        def bfs(r, c):
            area = 1
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row, col = q.popleft()
                direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in direct:
                    r, c = row + dr, col + dc
                    if(r in range(rows) and
                       c in range(cols) and
                       grid[r][c] == 1 and
                       (r, c) not in visit):
                        area += 1
                        q.append((r,c))
                        visit((r,c))
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    res = max(res, bfs(r, c))
        return res