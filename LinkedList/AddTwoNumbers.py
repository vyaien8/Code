# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        res = ListNode()
        tail = res
        left = 0
        while l1 and l2:
            k = l1.val + l2.val + left
            left = 0
            l1, l2 = l1.next, l2.next
            if k >= 10:
                left = 1
                k -= 10
            tail.next = ListNode(k, None)
            tail = tail.next
        while l1:
            k = l1.val + left
            left = 0
            l1 = l1.next
            if k >= 10:
                left = 1
                k -= 10
            tail.next = ListNode(k, None)
            tail = tail.next
        while l2:
            k = l2.val + left
            left = 0
            l2 = l2.next
            if k >= 10:
                left = 1
                k -= 10
            tail.next = ListNode(k, None)
            tail = tail.next
        if left:
            tail.next = ListNode(left, None)
            tail = tail.next
        return res.next
        