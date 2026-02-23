class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        res = 0
        l = 0
        dicts = set()
        for r in range(len(s)):
            while s[r] in dicts:
                dicts.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            dicts.add(s[r])
        return res