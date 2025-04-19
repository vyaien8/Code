from heapq import *
class KthLargest:

    def __init__(self, k: int, nums: [int]):
        self.k = k
        heapify(nums)
        while len(nums) > k:
            heappop(nums)
        self.h = nums

    def add(self, val: int) -> int:
        heappush(self.h, val)
        if len(self.h) > self.k:
            heappop(self.h)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4,5,8,2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
