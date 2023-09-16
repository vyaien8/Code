class Solution(object):
    def containsDuplicate(self, nums):
        snums = set(nums)
        if len(snums) != len(nums):
            return True
        else:
            return False
