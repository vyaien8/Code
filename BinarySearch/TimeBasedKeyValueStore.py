class TimeMap():
    def __init__(self):
        self.m = {} # key : [(timestamp, value)]

    def search(self, a, x): #find index of biggest integer that smaller or equal x in array a
        l, r = 0, len(a) - 1
        res = -1
        while l <= r:
            m = l + (r - l) // 2
            if a[m][0] <= x:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res
    def set(self, key, value, timestamp):
        if key in self.m:
            self.m[key].append((timestamp, value))
        else:
            self.m[key] = []
            self.m[key].append((timestamp, value))
    def get(self, key, timestamp):
        if key in self.m:
            # find the biggest prev_timestamp that smaller or equal timestamp
            index = self.search(self.m[key], timestamp)
            if index == -1: # timestamp has no prev
                return "" 
            else:
                return self.m[key][index][1]
        else: # key not found
            return ""
        
