# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid_helper(root, left_max=float('-inf'), right_max=float('inf')):
            if not root:
                return True
            
            if root.val <= left_max or root.val >= right_max:
                return False
            
            return (valid_helper(root.left, left_max, root.val)
            and valid_helper(root.right, root.val, right_max))
        
        return valid_helper(root)

            