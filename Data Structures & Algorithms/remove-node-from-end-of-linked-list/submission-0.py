# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num_nodes = 0
        node = head

        while node:
            node = node.next 
            num_nodes +=1
        
        remove_indx = num_nodes - n
        i = 0
        node = head
        while i <= remove_indx:
            if remove_indx == 0:
                head = head.next
                return head
            elif i == remove_indx-1:
                node.next = node.next.next
                break
            
            node = node.next
            i+= 1
        
        return head