# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, path_max):
            nonlocal res
            if not node:
                return
            if node.val >= path_max:
                res += 1
            dfs(node.left, max(node.val, path_max))
            dfs(node.right, max(node.val, path_max))
        
        dfs(root, float('-inf'))
        return res