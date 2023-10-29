def canPartition(self, nums: [int]) -> bool: # can divide array into partition that sum equal each other
        total = sum(nums)
        if total % 2 == 1:
            return False
        total //=2
        s = set()
        s.add(0)
        for i in nums:
            nexts = set()
            for j in s:
                if j + i == total:
                    return True
                nexts.add(j)
                nexts.add(j + i)
            s = nexts