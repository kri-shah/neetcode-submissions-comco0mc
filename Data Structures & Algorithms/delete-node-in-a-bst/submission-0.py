# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, key):
            if not node:
                return
            
            if key < node.val:
                node.left = dfs(node.left, key)
            elif key > node.val:
                node.right = dfs(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    curr = node.right
                    while curr.left:
                        curr = curr.left
                    node.val = curr.val 
                    node.right = dfs(node.right, curr.val)
            return node
        return dfs(root, key)

