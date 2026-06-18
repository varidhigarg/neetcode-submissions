# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def bfs(root, res, k):
            if not root:
                return
            bfs(root.left, res, k)
            res.append(root.val)
            bfs(root.right, res, k)
        
        res = []
        bfs(root, res, k)
        return res[k-1]
            