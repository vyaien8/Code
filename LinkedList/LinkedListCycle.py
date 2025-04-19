# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Floyd's Tortoise & Hare
# the idea is there are a slow and a fast pointer
# if there no loop, the fast pointer will reach the null pointer first
# else the faster pointer will stuck in the loop and at a time, the slow pointer will reach the loop and they meet each other
# they have to meet each other because:
# suppose the gap between them when the slow reach the first point of the loop is x
# each time the gap will be gap + 1 - 2 (because we move each interator, fast pointer moves 2 and slow moves 1)
# eventually, gap will be 0 and they meet each other 
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