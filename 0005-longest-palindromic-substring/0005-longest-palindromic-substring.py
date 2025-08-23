class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def isValid(l, r):
            while l >= 0 and r < len(s) and s[r] == s[l]:
                l, r = l - 1, r + 1
            return s[l + 1 : r]
        for i in range(len(s)):
            temp1 = isValid(i, i)
            temp2 = isValid(i, i + 1)
            if len(temp1) > len(res):
                res = temp1
            if len(temp2) > len(res):
                res = temp2
        return res