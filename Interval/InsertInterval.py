class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        if not intervals:
            return [newInterval]
        res = []
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            elif intervals[i][0] > newInterval[1]: # done
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        res.append(newInterval)
        return res

