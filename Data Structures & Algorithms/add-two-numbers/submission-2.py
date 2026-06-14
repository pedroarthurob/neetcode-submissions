# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def ListNodeToNumber(node):
            number = node.val
            node = node.next
            i = 1 
            while node:
                number = number + node.val * (10 ** i) 
                node = node.next
                i += 1

            print(number)
            return number
        
        def NumberToListNode(number):
            dummy = ListNode()
            current = ListNode(val = number % 10)
            dummy.next = current

            number = number // 10
            while number > 0:
                current.next = ListNode(val = number % 10)
                number = number // 10
                current = current.next

            return dummy.next
        
        return NumberToListNode(ListNodeToNumber(l1) + ListNodeToNumber(l2))