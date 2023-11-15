from heapq import *
class Solution:
    def networkDelayTime(self, times: [[int]], n: int, k: int) -> int:
        edges = {i:[] for i in range(1, n + 1)}
        for u, v, w in times:
            edges[u].append((v, w))
        #start at k
        djik = [float("inf")] * (n + 1) # just for learning djikstra algorithm
        djik[k] = 0 # from k to k is zero
        visit = set()
        minH = [(0, k)]
        res = 0
        while minH:
            w, u = heappop(minH)
            if u in visit:
                continue
            visit.add(u)
            djik[u] = w
            res = max(res, w)
            for nei, neiW in edges[u]:
                if nei not in visit:
                    heappush(minH, (neiW + w, nei))
        print(djik[1:])
        return res if len(visit) == n else -1
test = Solution()
test.networkDelayTime([[1,2,4], [1,3,1], [3,4,1], [4,2,1]], 4, 1)