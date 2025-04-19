from heapq import *
class Solution:
    def minCostConnectPoints(self, points: [[int]]):
        n = len(points) # number node
        adj = {i:[] for i in range(n)}
        # build the list for each point with length to their nei
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dis = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dis, j])
                adj[j].append([dis, i])
        # prim's
        res = 0
        visit = set()
        #start with point 0
        minH = [[0,0]] # [dis, point]
        while len(visit) < n:
            cost, point = heappop(minH)
            if point in visit:
                continue
            visit.add(point)
            res += cost
            for neiCost, nei in adj[point]:
                if nei not in visit:
                    heappush(minH, [neiCost, nei])
        return res
