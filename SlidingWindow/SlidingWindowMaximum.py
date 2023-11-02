from collections import *
class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        q = deque() # the first element always the maximum of current window
        l, r = 0, 0
        while r < k:
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            r += 1
        res.append(nums[q[0]])
        while r < len(nums):
            l += 1 # next window
            if l > q[0]: # if the max not in current window
                q.popleft()
            while q and nums[r] > nums[q[-1]]: # pop until the max of current window is on top
                q.pop()
            q.append(r)
            r += 1
            res.append(nums[q[0]])
        return res

test = Solution()
print(test.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
            
            
        
            
