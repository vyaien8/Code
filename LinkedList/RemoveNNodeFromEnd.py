# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        def size(head):
            res = 0
            while head:
                res += 1
                head = head.next
            return res
        sz = size(head)
        if sz == 1:
            return None
        if sz == n:
            return head.next
        cur = head
        n = sz - n - 1
        while n:
            n -= 1
            cur = cur.next
        cur.next = cur.next.next
        return head

    # two pointer 
    # right pointer run n time the left to reach null is size - n
    # left pointer point to head also need size - n to reach the node before the one we want to delete 
    def removeNthFromEnd2(self, head, n):
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0:
            n -= 1
            right = right.next
        while right:
            right = right.next
            left = left.next
        left.next  = left.next.next
        return dummy.next