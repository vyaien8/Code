class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l1, l2 = len(nums1), len(nums2)
        total = l1 + l2
        half = total // 2
        if l2 < l1:
            nums1, nums2 = nums2, nums1
            l1, l2 = l2, l1
        l, r = 0, l1 - 1
        while True:
            m = (l + r) // 2
            n = half - m - 2 # -2 for correct index of nums2 because 0-indexing default by list() 
            left1 = nums1[m] if m >= 0 else float("-infinity")
            right1 = nums1[m + 1] if (m + 1) < l1 else float("infinity")
            left2 = nums2[n] if n >= 0 else float("-infinity")
            right2 = nums2[n + 1] if (n + 1) < l2 else float("infinity")

            if left1 <= right2 and left2 <= right1:
                if total % 2: # odd total elements
                    return min(right1, right2)
                else: # even total elements
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r = m - 1
            else:
                l = m + 1