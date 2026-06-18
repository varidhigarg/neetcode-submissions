# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        value = preorder[0]
        root = TreeNode(value)

        idx = inorder.index(value)
        left = inorder[:idx]
        right = inorder[idx+1:]
        left_pre = preorder[1:len(left)+1]
        right_pre = preorder[len(left)+1:]
        root.left = self.buildTree(left_pre, left)
        root.right = self.buildTree(right_pre, right)
        return root
