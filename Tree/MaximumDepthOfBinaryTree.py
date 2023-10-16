# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # DFS
    def maxDepth(self, root: TreeNode):
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return 0
    def maxDepth3(self, root: TreeNode):
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = depth
                stack.append([node.left, res])
                stack.append([node.right, res])
        return res
    # BFS: for each level pop them and append their children
    def maxDepth2(self, root: TreeNode):
        if not root:
            return 0
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

