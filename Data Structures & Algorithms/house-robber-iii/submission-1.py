# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(node, can_rob):
            key = (node, can_rob)
            if key in memo:
                return memo[key]
            
            if not node:
                return 0 
            
            best = dfs(node.left, True) + dfs(node.right, True)
            if can_rob:
                best = max(best, node.val + dfs(node.left, False) + dfs(node.right, False))
            
            memo[key] = best
            
            return memo[key]
        
        return dfs(root, True)
