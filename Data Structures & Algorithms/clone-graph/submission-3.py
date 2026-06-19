"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def getNode(self, val):
        if val not in self.data:
            self.data[val] = Node(val)
        return self.data[val]
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        self.data = {}
        visited = set()
        tovisit = [node]
        while tovisit:
            node = tovisit.pop()
            if node.val in visited:
                continue
            new_node = self.getNode(node.val)
            visited.add(node.val)
            for neigh in node.neighbors:
                new_node.neighbors.append(self.getNode(neigh.val))
                if neigh.val not in visited:
                    tovisit.append(neigh)
            
        return self.data[1]
        