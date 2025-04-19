from collections import deque
class Solution:
    def pacificAtlantic(self, heights: [[int]]):
        if not heights:
            return [[]]
        rows, cols = len(heights), len(heights[0])
        res = []
        dp = {}
        def bfs(r, c):
            pacific = False
            atlantic = False
            visit = set()
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while q:
                row, col = q.popleft()
                for dr, dc in dir:
                    r, c = row + dr, col + dc
                    if r == rows or c == cols:
                        atlantic = True
                    if r < 0 or c < 0:
                        pacific = True
                    if atlantic and pacific:
                        return True
                    if r in range(rows) and c in range(cols) and heights[row][col] >= heights[r][c] and (r, c) not in visit:
                        q.append((r,c))
                        visit.add((r, c))
            return pacific and atlantic
        for r in range(rows):
            for c in range(cols):
                if bfs(r, c):
                    res.append([r, c])
        return res
    def pacificAtlantic2(self, h: [[int]]):
        rows, cols = len(h), len(h[0])
        pac, atl = set(), set()
        def dfs(r, c, visit, preHeight):
            if( (r, c) in visit or
               r < 0 or
               c < 0 or
               r == rows or
               c == cols or
               h[r][c] < preHeight # if the current height less than the prev, it can not let the flow into the prev
            ):
                return
            visit.add((r, c))
            dfs(r - 1, c, visit, h[r][c])
            dfs(r + 1, c, visit, h[r][c])
            dfs(r, c + 1, visit, h[r][c])
            dfs(r, c - 1, visit, h[r][c])
        for c in range(cols):
            dfs(0, c, pac, h[0][c])
            dfs(rows -1, c, atl, h[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pac, h[r][0])
            dfs(r, cols - 1, atl, h[r][cols - 1])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res