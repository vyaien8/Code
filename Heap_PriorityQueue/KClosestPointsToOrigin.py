from heapq import *
class Solution:
    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        dis = []
        res = []
        for i in range(len(points)):
            dis.append((points[i][0] ** 2 + points[i][1] ** 2, i))
        heapify(dis)
        while k:
            tmp = heappop(dis)
            res.append(points[tmp[1]])
            k -= 1
        return res