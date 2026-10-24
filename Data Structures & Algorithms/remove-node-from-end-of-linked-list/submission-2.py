# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # n = 2
        # 1 2 3 4 
        # 1, 3
        # 2, 4
        # 3, None
        p1 = head
        p2 = head
        for _ in range(n):
            p2 = p2.next
        
        if p2:
            while p2.next:
                print(f"{p1.val} : {p2.val}")
                p1 = p1.next
                p2 = p2.next
            p1.next = p1.next.next
        else:
            return p1.next
        
        
        return head
        