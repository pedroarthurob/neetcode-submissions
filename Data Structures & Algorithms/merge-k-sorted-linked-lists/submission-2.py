# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:

            dummy = ListNode()
            currentNode = dummy
            while list1 or list2:
                if not list2 or (list1 and list1.val <= list2.val):
                    currentNode.next = list1
                    list1 = list1.next

                else:
                    currentNode.next = list2
                    list2 = list2.next
                
                currentNode = currentNode.next
            
            return dummy.next

        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i], lists[i-1])

        return lists[-1]