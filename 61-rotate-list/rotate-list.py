# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return head
        #getting length 
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        curr = head  # move to the pivot and rotate
        for i in range  (length - k - 1):
            curr = curr.next
        newCurr = curr.next 
        curr.next = None 
        tail.next = head

        return newCurr