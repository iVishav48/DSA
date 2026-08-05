class Solution(object):
    def findWordsContaining(self, words, x):
        res = []
        for i in range (len(words)):
            for j in words[i]:
                if j == x:
                    res.append (i)
                    break
        return res
