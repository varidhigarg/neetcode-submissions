# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calcTree(self, root):
        if not root:
            return 0
        left = self.calcTree(root.left)
        right = self.calcTree(root.right)
        self.res = max((left + root.val + right) , self.res)
        node_sum = max(left, right) + root.val
        return node_sum if node_sum > 0 else 0
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        self.calcTree(root)
        return self.res
        
        