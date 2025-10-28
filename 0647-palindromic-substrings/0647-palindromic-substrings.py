class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPali(l, r):
            temp = 0
            while l >= 0 and r < len(s) and s[r] == s[l]:
                temp += 1
                l, r = l - 1, r + 1
            return temp
        res = 0
        for i in range(len(s)):
            res += isPali(i, i)
            res += isPali(i, i + 1)
        return res