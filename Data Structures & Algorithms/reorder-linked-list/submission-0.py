# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        snd = slow.next
        slow.next = None    

        prev = None
        curr = snd

        while curr: 
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt    

        snd = prev #head of reversed list

        first = head
        while snd: 
            tmp1 = first.next
            tmp2 = snd.next
            first.next = snd
            snd.next = tmp1
            first = tmp1
            snd = tmp2     
