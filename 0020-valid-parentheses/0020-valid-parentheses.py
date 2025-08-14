class Solution:
    def isValid(self, s: str) -> bool:
        close = { "}":"{", "]":"[",")":"("}
        res = []
        for c in s:
            if c in close:
                if res and res[-1] == close[c]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)
        return len(res) == 0