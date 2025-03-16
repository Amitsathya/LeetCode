class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 : return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        have, need = 0, len(countT)
        l, res, resLen = 0, [-1, -1], float("inf")
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0 ) + 1
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = [l, r]

                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""

        