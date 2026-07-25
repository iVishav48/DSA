class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # Step 1: Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Compare both halves
        first = head
        second = prev

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True