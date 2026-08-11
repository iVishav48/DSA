class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        min_length = min(len(s) for s in strs)

        for i in range(min_length):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return strs[0][:i]

        return strs[0][:min_length]