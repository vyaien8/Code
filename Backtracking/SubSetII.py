class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        nums.sort()
        res = []
        def bk(i, subset):
            if i == len(nums):
                subset.append(subset)
                # if subset[:] not in res:
                #     res.append(subset[:])
                return
            # subset include atleast a nums[i]
            subset.append(nums[i])
            bk(i + 1, subset)
            subset.pop()
            # subset not include any nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]: # find the last index of nums[i]
                i += 1
            bk(i + 1, subset)
            # bk(i + 1, subset)
        bk(0, [])
        return res