# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        
        q = deque()
        tq = deque()
        tq.append(root)
        q.append(tq)
        
        res = []
        while q:
            tq = q.popleft()
            nq = deque()
            t_list = []
            
            while tq:
                node = tq.popleft()
                t_list.append(node.val)
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            if nq:
                q.append(nq)
            res.append(t_list)
        
        return res
        