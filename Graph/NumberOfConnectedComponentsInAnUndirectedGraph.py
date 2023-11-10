class Solution:
    def countComponents(self, n: int, edges: [[int]]):
        par = [i for i in range(n)]
        rank = [1] * n
        def findP(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        def union(n1, n2):
            p1, p2 = findP(n1), findP(n2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res