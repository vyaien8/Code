# nums[n + 1] has all element in range [1, n]
# only one element is duplicated (has more than 1 in this array)
# find this element
# idea is, assume a[i] is the next node of the i node
# using Floyd algorithm to find the loop
# using math, can conclude that
# from the node where fast pointer meets the first slow pointer to the result node
# equal to distance from head to that node
class Solution:
    def findDuplicate(self, nums):
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        