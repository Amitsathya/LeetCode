class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs[1:]:
                if len(s) == i or s[i] != c:
                    return s[:i]
        return strs[0]
