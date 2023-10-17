# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return [True, 0] # return [current node status, hight of node]
            left, right = dfs(root.left), dfs(root.right)
            return [left[0] and right[0 and abs(left[1] - right[1]) <= 1], 1 + max(left[1], right[1])]
        return dfs(root)[0]