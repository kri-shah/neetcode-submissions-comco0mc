# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = []
        q = deque()
        q.append(root)
        while q:
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    serialized.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else:
                    serialized.append("N")

        
        return ",".join(serialized)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        vals = data.split(',')
        if vals[0] == "N":
            return None
        
        root = TreeNode(int(vals[0]))
        q = deque([root])
        
        i = 1
        while q and i < len(vals):
            node = q.popleft()
            
            if vals[i] != "N":
                left_node = TreeNode(int(vals[i]))
                node.left = left_node
                q.append(left_node)
            i += 1

            
            if i < len(vals):
                if vals[i] != "N":
                    right_node = TreeNode(int(vals[i]))
                    node.right = right_node
                    q.append(right_node)
                i += 1

        return root


