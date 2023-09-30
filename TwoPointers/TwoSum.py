class Solution:
    def twoSum(self, num, target):
        i, j = 0, len(num) - 1
        while i < j:
            s = s[i] + s[j]
            if s == target:
                return [i + 1, j + 1]
            elif s > target:
                j -= 1
            else:
                i += 1