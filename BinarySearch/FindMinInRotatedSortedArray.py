class Solution:
    # 4 5 6    1 2 3 
    # the rightmost element in the array is the key
    # if an element is smaller than or equal it, which mean it in smaller part, in this case we search on the left side to find the smaller
    # else it in the bigger part, we find on the right side to find the smaller 
    def findMin(self, a):
        n = len(a)
        l, r = 0, n - 1
        ans = -1
        while l <= r:
            m = l + (r - l) // 2
            if a[m] <= a[n - 1]:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return a[ans]