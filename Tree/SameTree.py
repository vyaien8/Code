# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def isSame(a, b):
            if a == None:
                return b == None
            if b == None:
                return False
            return a.val == b.val
        if isSame(p, q) == False:
            return False
        if p and q:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif q == None and q == None:
            return True
        return False
    def isSameTree2(self, p, q):
        if not p and not q:
            return True
        if q and p:
            return q.val == p.val and self.isSameTree2(q.left, p.left) and self.isSameTree2(q.right, p.right)
        return False