"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_mapping = dict()
        
        curr = head
        while curr:
            new_node = Node(curr.val)
            node_mapping[curr] = new_node
            curr = curr.next
        
        curr = head
        while curr:
            new_node = node_mapping[curr]
            new_node.next = node_mapping.get(curr.next)
            new_node.random = node_mapping.get(curr.random)
            curr = curr.next
            new_node = new_node.next

        return node_mapping.get(head) if not None else []




