# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        nextNode = current

        while current:
            nextNode = nextNode.next  
            current.next = previous
            previous = current
            current = nextNode
          

        return previous
        