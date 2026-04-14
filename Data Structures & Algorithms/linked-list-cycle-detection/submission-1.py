# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        n1 = head
        n2 = head
        while n1 and n2:
            n1 = n1.next
            if n2.next:
                n2 = n2.next.next 
            else:
                return False
            if n1 == n2:
                return True
        return False

