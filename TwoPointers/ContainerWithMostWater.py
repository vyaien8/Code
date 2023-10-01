class Solution:
    def maxArea(self, height):
        res = 0
        i, j = 0, len(height) - 1
        # area = (j - i) * min(height[i], height[j])
        # always change index of column has shorter height
        # because width always decrease by one each interator
        # heigher column seems has better area
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res