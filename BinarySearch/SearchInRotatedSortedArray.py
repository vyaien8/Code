class Solution:
    # return the index of target if found else return -1
    def search(self, nums, target):
        def binsearch(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return -1
        n = len(nums)
        l, r = 0, n - 1
        deli = -1
        # find the minimum index from that which is point seperate the array into 2 sorted array
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] <= nums[n - 1]:
                deli = m
                r = m - 1
            else:
                l = m + 1
        if nums[deli] == target:
            return deli
        elif nums[n - 1] > target: # if the biggest of the right part is bigger than target
            # which mean target lies on [deli, n] 
            i =  binsearch(nums[deli:], target)
            return -1 if i == -1 else deli + i # the correct index with origin array is deli + return index from binsearch
        else:
            return binsearch(nums[:deli], target) # first part (right part) with correct index with origin array