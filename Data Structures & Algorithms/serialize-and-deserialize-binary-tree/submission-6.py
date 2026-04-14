# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    res.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append("N")
        return "-".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree = data.split('-')
        if tree[0] == "N":
            return None
        
        root = TreeNode(int(tree[0]))
        queue = deque([root])
        i = 1
        while queue and i < len(tree):
            node = queue.popleft()
            if tree[i] != 'N':
                node.left = TreeNode(int(tree[i]))
                queue.append(node.left)
            i += 1
            if tree[i] != 'N':
                node.right = TreeNode(int(tree[i]))
                queue.append(node.right)
            i += 1
        
        return root



