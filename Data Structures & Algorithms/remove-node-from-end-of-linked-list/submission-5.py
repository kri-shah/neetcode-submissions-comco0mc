class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p1 = p2 = dummy

        for _ in range(n):
            p2 = p2.next

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next
        return dummy.next