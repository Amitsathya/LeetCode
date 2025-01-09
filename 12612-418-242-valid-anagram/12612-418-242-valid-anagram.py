class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charT, charS = [0]*26,[0]*26
        print(charT)
        for i in range(0, len(s)):
            charT[ord(t[i])-ord('a')] += 1
            charS[ord(s[i])-ord('a')] += 1
        return charT == charS

        