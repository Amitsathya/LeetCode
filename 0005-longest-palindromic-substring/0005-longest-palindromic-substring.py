class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            temp1 = self.checkPalindrome(s, i, i)
            temp2 = self.checkPalindrome(s, i, i + 1)
            if len(temp1) > len(res):
                res = temp1
            if len(temp2) > len(res):
                res = temp2
        return res

    
    def checkPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]
        