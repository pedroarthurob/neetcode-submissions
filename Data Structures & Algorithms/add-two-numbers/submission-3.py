# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        
        current_node = dummy
        carry = 0
        while l1 or l2 or carry > 0:
            current_sum = carry

            if l1:
                current_sum += l1.val
                l1 = l1.next

            if l2:
                current_sum += l2.val
                l2 = l2.next

            carry = current_sum // 10
            current_sum = current_sum % 10
            current_node.next = ListNode(val=current_sum)
            current_node = current_node.next 


        return dummy.next