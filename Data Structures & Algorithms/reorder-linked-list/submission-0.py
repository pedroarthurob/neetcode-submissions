# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # First, find the middle using fast and slow
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now I've found the middle, which is slow.next
        # now I need to reverse the second half
        previous = None
        current = slow.next
        slow.next = None
        
        while current:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode

        # Now it's reversed and the previous is the head of
        # this reversed list
        # Now I need to merge the head and the previous
        list1 = head
        list2 = previous

        while list1 and list2:
            nextNode1 = list1.next
            nextNode2 = list2.next

            list1.next = list2
            list2.next = nextNode1

            list1 = nextNode1
            list2 = nextNode2