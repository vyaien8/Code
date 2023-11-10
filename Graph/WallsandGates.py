from collections import deque
class Solution:
    def wallsAndGates(self, rooms: [[int]]):
        rows, cols = len(rooms), len(rooms[0])
        visit = set()
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c,0))
                    visit.add((r,c))
        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            row, col, level = q.popleft
            level += 1
            for dr, dc in d:
                r, c = row + dr, col + dc
                if (r in range(rows) and
                    c in range(cols) and
                    (r,c) not in visit and
                    rooms[r][c] != -1):
                    rooms[r][c] = level
                    visit.add(r,c)
                    q.append(r,c,level)
