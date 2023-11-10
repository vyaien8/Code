class Solution:
    def rotate(self, matrix: [[int]]):
        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
            # left     # right
    #top        # # # #
                # # # #
                # # # #
    #bottom     # # # #
        while top < bottom and left < right:
            prev = matrix[top + 1][left]
            for c in range(left, right + 1):
                matrix[top][c], prev = prev, matrix[top][c]
            top += 1
            for r in range(top, bottom + 1):
                matrix[r][right], prev = prev, matrix[r][right]
            right -= 1
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    matrix[bottom][c], prev = prev, matrix[bottom][c]
                bottom -= 1
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    matrix[r][left], prev = prev, matrix[r][left]
                left += 1
        return
test = Solution()
print(test.rotate([[1,2,3], [8,9,4], [7,6,5]]))            