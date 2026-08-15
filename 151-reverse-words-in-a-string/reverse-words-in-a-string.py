class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        reverse = reversed(words)
        res = " ".join(reverse)
        return res