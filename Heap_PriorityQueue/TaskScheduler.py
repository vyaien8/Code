from heapq import *
from collections import deque
class Solution:
    def leastInterval(self, tasks: [str], n: int):
        res = 0
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1
        counts = list(counts.values())
        for i in range(len(counts)):
            counts[i] *= -1
        heapify(counts)
        q = deque()
        while counts or q:
            if q and res == q[0][1]:
                heappush(counts, q[0][0])
                q.popleft()               
            res += 1
            if counts:
                a = heappop(counts)
                a += 1
                if a:
                    q.append((a, res + n))
        return res
test = Solution()
test.leastInterval(["A","A","A","B","B","B"], 2)
