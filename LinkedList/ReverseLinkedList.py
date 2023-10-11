# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        if head == None:
            return head
        prev = None
        cur = head
        while cur != None:
            n = cur.next
            cur.next = prev
            prev, cur = cur, n
        return prev
    