class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0: return ""
        countT, window = {}, {}
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1
        l, resLen, res = 0, float('inf'), [-1, -1]
        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in countT and countT[c] == window[c]:
                have += 1
            while have == need:
                c = s[l]
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if c in countT and countT[c] > window[c]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float('inf') else ""



