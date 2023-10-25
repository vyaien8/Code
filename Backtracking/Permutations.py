class Solution:
    def permute(self, nums):
        result = []
        if len(nums) == 1:
            return [nums[:]] # return it self
        for i in range(len(nums)):
            n = nums.pop(0) # pop the first element , can use deque or better performent
            perms = self.permute(nums) # divide into subproblem 
            for perm in perms: # conquer 
                perm.append(n)
            result.extend(perms)
            nums.append(n) # backtrack
        return result
