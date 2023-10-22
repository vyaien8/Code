# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def DFS(root, maxVal):
            if not root:
                return 0
            res = 1 if root.val >= maxVal else 0
            maxVal = max(maxVal, root.val)
            res += DFS(root.left, maxVal)
            res += DFS(root.right, maxVal)
            return res
        return DFS(root, root.val)