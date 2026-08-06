# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        def mergeTwoLists(l1, l2):
            dummy = start = ListNode(0)
            
            while l1 and l2: 
                if l1.val < l2.val: 
                    start.next = l1
                    l1 = l1.next
                else: 
                    start.next = l2
                    l2 = l2.next
                start = start.next

            start.next = l1 or l2
            return dummy.next

        merged = None 

        for head in lists: 
            merged = mergeTwoLists(merged, head)
 

        return merged
                    