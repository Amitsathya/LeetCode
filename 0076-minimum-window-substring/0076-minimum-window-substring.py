class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0: return ""
        window, countT = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        have, need = 0, len(countT)
        res, resLen, l = [-1, -1], float("infinity"), 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in countT and countT[c] == window[c]:
                have += 1
            while have == need:
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] <countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""