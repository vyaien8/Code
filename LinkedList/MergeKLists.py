# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        def merge(l1, l2):
            head = ListNode()
            cur = head
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            return head.next
        if not lists:
            return None
        res = None
        for l in lists:
            res = merge(res, l)
        return res
    # effective way with merge sort
    def mergeKLists2(self, lists):
        def merge(l1, l2):
            head = ListNode()
            cur = head
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            return head.next
        n = len(lists)
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mLists.append(merge(l1, l2))
            lists = mLists
        return lists[0]
        