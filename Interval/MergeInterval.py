class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(intervals[i][1], res[-1][1])
        return res