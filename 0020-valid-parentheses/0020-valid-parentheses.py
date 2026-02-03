class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        dicts = {"]": "[", "}": "{", ")": "("}
        for c in s:
            if c in dicts:
                if res and res[-1] == dicts[c]:
                    res.pop()
                else:                    
                    return False
            else:
                res.append(c)
        return len(res) == 0