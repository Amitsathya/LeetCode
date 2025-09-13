class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []

        def genParen(closeN, openN):
            if closeN == openN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                genParen(closeN, openN + 1)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                genParen(closeN + 1, openN)
                stack.pop()
        genParen(0, 0)
        return res