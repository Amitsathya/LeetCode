class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPali(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return s[l + 1: r]
        res = ""
        for i in range(len(s)):
            temp1 = isPali(i, i)
            temp2 = isPali(i, i + 1)
            if len(res) < len(temp1):
                res = temp1
            if len(res) < len(temp2):
                res = temp2
        return res