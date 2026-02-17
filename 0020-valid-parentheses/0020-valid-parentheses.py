class Solution:
    def isValid(self, s: str) -> bool:
        paren = {"}":"{", "]":"[", ")":"("}
        stack = []
        for c in s:
            if c in paren:
                if stack and stack[-1] == paren[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False
