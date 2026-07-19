class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s)-1
        while left <= right:
            s[right], s[left] = s[left],s[right]  
            right -=1
            left +=1
        return s