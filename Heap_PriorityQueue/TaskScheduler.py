from heapq import *
from collections import deque
class Solution:
    def leastInterval(self, tasks: [str], n: int):
        res = 0
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1
        counts = list(counts.values())
        # create the maxheap which store number of times each task have to take
        for i in range(len(counts)):
            counts[i] *= -1
        heapify(counts)
        q = deque() # (left, time) store the number of times a task left and the time it can redo  
        while counts or q:
            if q and res == q[0][1]: # if current time is the time the job can redo
                heappush(counts, q[0][0])
                q.popleft()               
            res += 1
            if counts: 
                a = heappop(counts)
                a += 1
                if a:
                    q.append((a, res + n)) # res is current time, n is the cooldown to do a same task again
        return res
test = Solution()
test.leastInterval(["A","A","A","B","B","B"], 2)
