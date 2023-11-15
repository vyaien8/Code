class Solution:
    def permute(self, nums):
        result = []
        if len(nums) == 1:
            return [nums[:]] # return it self
        for i in range(len(nums)):
            n = nums.pop(0) # pop the first element, append it to the end latter
            perms = self.permute(nums) # divide into subproblem 
            for perm in perms: # conquer, for each perm get from the left array after pop n 
                perm.append(n) # add n to complete the permutation
            result.extend(perms)
            nums.append(n) # backtrack, restore n to it to the end of nums
        return result
