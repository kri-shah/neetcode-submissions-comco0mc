# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        order = defaultdict(list)
        
        def bfs(node, index):
            l = float('inf')
            r = float('-inf')
            q = deque()
            q.append((node, index))
            while q:
                node, i = q.popleft()
                l = min(i, l)
                r = max(i, r)
                order[i].append(node.val)
                if node.left:
                    q.append((node.left, i-1))
                if node.right:
                    q.append((node.right, i+1))
            
            return (l, r)
        
        l, r = bfs(root, 0)
        res = [order[i] for i in range(l, r+1)]
        
        return res
