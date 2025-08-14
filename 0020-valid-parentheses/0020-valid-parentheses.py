class Solution:
    def isValid(self, s: str) -> bool:
        parenMap = {"]":"[", "}":"{", ")":"("}
        stack = []
        for c in s:
            if c in parenMap:
                if stack and stack[-1] == parenMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False