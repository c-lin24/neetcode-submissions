# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr: 
            curr = curr.next
            length += 1

        steps = length - n
        cnt = 0
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(steps):
            prev = prev.next

        prev.next = prev.next.next
        return dummy.next
        
