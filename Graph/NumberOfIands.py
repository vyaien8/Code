from collections import deque
class Solution:
    def numberIslands(self, grid: [[int]]):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        # dfs
        def dfs(r, c):
            if (r not in range(rows)
                or c not in range(cols)
                or (r, c) in visit
                or grid[r][c] == '0'):
                return
            visit.add((r, c))
            direct = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for i, j in direct:
                dfs(r + i, c + j)

        # bfs
        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row, col = q.popleft()
                direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in direct:
                    r, c = row + dr, col + dc
                    if ( r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == '1' and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands
    

