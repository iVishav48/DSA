# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        prev = ListNode (0,head)
        left = prev 
        right = head
        #while n and right:
        for i in range(n):
            right = right.next 
            n-=1

        while right:
            left = left.next 
            right = right.next 
        
        left.next = left.next.next 

        return prev.next 