from heapq import *
class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        heapify(nums)
        while len(nums) != k:
            heappop(nums)
        return nums[0]     
        