# Definition for a Node.
class Node:
    def __init__(self, x, next, random):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head):
        oldToCopy = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]