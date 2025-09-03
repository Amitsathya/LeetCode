class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {'}' : '{', "]" : "[", ")":"("}
        for c in s:
            if c in bracket:
                if stack and stack[-1] == bracket[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0