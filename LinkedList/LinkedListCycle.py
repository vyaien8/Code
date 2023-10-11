# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# the idea is there are a slow and a fast pointer
# if there no loop, the fast pointer will reach the null pointer first
# else the faster pointer will stuck in the loop and at a time, the slow pointer will reach the loop and they meet each other
class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False