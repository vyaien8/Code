# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: [TreeNode]) -> int:
        res = [root.val] # make it global

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # compute max path with split
            res[0] = max(res[0], root.val + max(0, leftMax)+ max(0, rightMax))
            return root.val + max(0, leftMax, rightMax)
        dfs(root)
        return res[0]
            