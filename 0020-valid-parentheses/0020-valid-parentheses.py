class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {"]":"[","}":"{",")":"("}
        for c in s:
            if c in hashMap:
                if stack and stack[-1] == hashMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0