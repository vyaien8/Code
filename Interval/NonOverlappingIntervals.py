class Solution:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        intervals.sort()
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[i - 1][1]:
                continue
            res += 1
            intervals[i][1] = min(intervals[i][1], intervals[i - 1][1])
        return res