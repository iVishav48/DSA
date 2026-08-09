class Solution(object):
    def reverseStr(self, s, k):
        i = 0
        s = list(s)
        while i < len(s):
            left = i  
            right = i + k - 1
            right = min(i + k - 1, len(s) - 1)
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            i += 2 * k
        return ''.join(s)