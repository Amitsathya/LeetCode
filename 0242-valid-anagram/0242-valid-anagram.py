class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        lenS, lenT = {}, {}
        for i in range(len(s)):
            lenS[s[i]] = lenS.get(s[i], 0) + 1
            lenT[t[i]] = lenT.get(t[i], 0) + 1
        return lenS == lenT
        