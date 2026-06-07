# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        for i in range(n):
            first = first.next

        dummy = ListNode(next=head)
        second = dummy
        while first:
            second = second.next
            first = first.next
        

        second.next = second.next.next

        return dummy.next