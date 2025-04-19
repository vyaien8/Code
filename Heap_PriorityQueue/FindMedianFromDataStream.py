from heapq import *
class MedianFinder:

    def __init__(self):
        self.maxheap, self.minheap = [], []
        # all value of maxheap <= all value of mean heap
        # |len(maxheap) - len(minheap)| <= 1 

    def addNum(self, num: int) -> None:
        if self.minheap and num >  self.minheap[0]: # if num is bigger than every number in maxheap (max maxheap <= min minheap = minheap[0])
            heappush(self.minheap, num)
        else:
            heappush(self.maxheap, -1 * num) 
        # |len(maxheap) - len(minheap)| <= 1
        if len(self.maxheap) > len(self.minheap) + 1:
            heappush(self.minheap, -1 * heappop(self.maxheap))
        if len(self.minheap) > len(self.maxheap) + 1:
            heappush(self.maxheap, -1 * heappop(self.minheap))
    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -1 * self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return (self.minheap[0] + -1 * self.maxheap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()