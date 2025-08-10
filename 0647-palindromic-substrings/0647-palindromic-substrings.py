class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def dfs(l, r):
            temp = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                temp += 1
                l, r = l - 1, r + 1
            return temp
        
        for i in range(len(s)):
            res += dfs(i, i)
            res += dfs(i, i + 1)
        return res