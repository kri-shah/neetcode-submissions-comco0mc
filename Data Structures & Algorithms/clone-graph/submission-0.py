"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_map = dict()
        def dfs(node):
            if node in clone_map:
                return clone_map[node]
            
            cloned = Node(node.val)
            clone_map[node] = cloned
            for neigh in node.neighbors:
                cloned.neighbors.append(dfs(neigh))
            
            return cloned

        return dfs(node) if node else None

