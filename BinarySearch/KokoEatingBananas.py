from math import *
class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles) # the minimum and maximum speed
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            time = 0
            for pile in piles: # cal time eat all banana with mid speed
                time += ceil(pile / mid)
            if time <= h: # if time under the limit h
                res = mid 
                r = mid - 1 # find on the left for the shorter speed
            else:
                l = mid + 1 # find on the right
        return res
