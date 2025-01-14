class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countT, countS = [0]*26, [0]*26
        for i in range(0, len(s)):
            countT[ord(t[i])-ord('a')]+=1
            countS[ord(s[i])-ord('a')]+=1
        return countT==countS
        