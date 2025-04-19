# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def preOrder(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)
        return ','.join(res)
    def deserialize(self, data):
        tree = data.split(',')
        self.i = 0
        def dfs():
            if tree[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(tree[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
            
           
           
       

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)
# ser = Codec()
# print(ser.serialize(root))