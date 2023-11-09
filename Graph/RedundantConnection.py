class Solution:
    def findRedundantConnection(self, edges: [[int]]) -> [int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        # find the root node
        def findP(node):
            p = par[node]
            while p != par[p]:
                par[p] = par[par[p]] # just for faster
                p = par[p]
            return p
        
        def union(n1, n2):
            p1, p2 = findP(n1), findP(n2)
            if p1 == p2: # if they already connect
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        