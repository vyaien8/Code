from collections import *
class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        q = deque()
        l, r = 0, 0
        while r < k:
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            r += 1
        res.append(nums[q[0]])
        while r < len(nums):
            l += 1
            if l > q[0]:
                q.popleft()
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            r += 1
            res.append(nums[q[0]])
        return res
            
            
        
            
