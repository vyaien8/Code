class Solution:
    def longestConsecutive(self, nums):
        snums = set(nums) # remove duplicate
        longest = 0
        for i in snums:
            if i - 1 not in snums:
                length = 1
                while i + length in snums:
                    length += 1
                longest = max(longest, length)
        return longest