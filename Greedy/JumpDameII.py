from collections import deque
class Solution:
    def jump(self, nums: [int]):
        res = 0
        l, r = 0, 0
        while r < len(nums) - 1: # while the farthest not reach the goal
            farthest = 0 # find the farthest the current window can jump
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res