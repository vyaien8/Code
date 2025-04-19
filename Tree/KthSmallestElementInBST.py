# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        x = [k]
        def DFS(root):
            if not root:
                return None
            left = DFS(root.left)
            if left:
                return left
            x[0] -= 1
            if x[0] == 0:
                return root
            return DFS(root.right)
        return DFS(root).val
    def kthSmallest2(self, root, k):
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        