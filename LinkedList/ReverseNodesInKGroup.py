# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        prevh = dummy
        while True:
            knode = self.getK(prevh, k)
            if not knode:
                return dummy.next
            n = knode.next
            prev, cur = n, prevh.next # we set prev is the next node of the knode
            while cur != n:
                nx = cur.next
                cur.next = prev
                prev, cur = cur, nx
            # knode is the head of  group k
            prevh.next, prevh = knode, prevh.next
    def getK(self, prev, k): # get the k node after prev
            while k > 0 and prev:
                k -= 1
                prev = prev.next
            return prev

        



        


