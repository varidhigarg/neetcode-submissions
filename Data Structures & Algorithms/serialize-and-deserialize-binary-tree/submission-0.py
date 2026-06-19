# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def bfs(root):
            queue = deque([root])
            res = []
            while queue:
                node = queue.popleft()
                if node:
                    res.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append("n")
            return res
        res = bfs(root)
        return ",".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dataArr = data.split(',')
        print(dataArr)
        if dataArr[0] == 'n':
            return
        root = TreeNode(int(dataArr[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if dataArr[index] != 'n':
                node.left = TreeNode(int(dataArr[index]))
                queue.append(node.left)
            index+=1
            if dataArr[index] != 'n':
                node.right = TreeNode(int(dataArr[index]))
                queue.append(node.right)
            index+=1
        return root
