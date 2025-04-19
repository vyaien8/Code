# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val < p.val and root.val < q.val: # both p and q are in the right of of current node
                root = root.right
            elif root.val > p.val and root.val > q.val: # both q and p are in the left side of current node
                root = root.left
            else:
                return root 