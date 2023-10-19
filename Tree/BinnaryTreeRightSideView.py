# idea is when perform BFS, the last node add each level is the rightmost node of them and also the node is seen from rightside
# we can perfrom with different orfer right first left after, we can see the left side of it
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: [TreeNode]) -> [int]:
        res = []
        q = deque([root])
        while q:
            rightSide = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res