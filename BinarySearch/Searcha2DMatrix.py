class Solution:
    # convert a 1 2DMatrix m[r][c] into a array a: a[i] = m[i // c][i % c]  
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False