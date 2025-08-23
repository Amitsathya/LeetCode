class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def isValid(l, r):
            length = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length += 1
                l, r = l - 1, r + 1
            return length
        
        for i in range(len(s)):
            res += isValid(i, i)
            res += isValid(i, i + 1)
        return res