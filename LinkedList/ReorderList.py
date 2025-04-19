# Definition for singly-linked list.
import collections
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # memory is not to good
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        q = collections.deque()
        cur = head.next
        while cur:
            q.append(cur)
            cur = cur.next
        cur = head
        while q:
            r = q.pop()
            r.next = None
            cur.next = r
            cur = cur.next
            if q:
                l = q.popleft()
                l.next = None
                cur.next = l
                cur = cur.next
    #without extra space
    #reverse the second haft of the list
    def reorderList2(self, head):
        def reverse(head):
            prev, cur = None, head
            while cur:
                n = cur.next
                cur.next = prev
                prev, cur = cur, n
            return prev
        # slit the list into second haft
        # the second haft start from slow.next
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #reverse the second haft
        second = reverse(slow.next)
        slow.next = None # make slow is the tail of first haft
        cur = head
        while second:
            n = cur.next
            cur.next = second
            second = second.next
            cur = cur.next
            cur.next = n
            cur = n
        
