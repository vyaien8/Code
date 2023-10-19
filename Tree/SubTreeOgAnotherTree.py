# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: [TreeNode], subRoot: [TreeNode]) -> bool:
        def isSame(a, b):
            if not a and not b:
                return True
            if a and b and a.val == b.val:
                return isSame(a.left, b.left) and isSame(a.right, b.right)
            return False
        if not subRoot:
            return True
        if root == None:
            return False
        if isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right)
    