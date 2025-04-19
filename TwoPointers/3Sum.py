class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0: # the left most must be negative because sum must equal 0
                break
            if i > 0 and a == nums[i - 1]: # remove dupplicate
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:    # two pointer to find the twosum equal -a
                s = a + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # update left pointer to find other solution with same value a
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res   