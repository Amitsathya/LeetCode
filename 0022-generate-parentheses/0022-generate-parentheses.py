class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def genParen(closedN, openedN):
            if closedN == n:
                res.append("".join(stack))
                return
            if openedN < n:
                stack.append("(")
                genParen(closedN, openedN + 1)
                stack.pop()
            if closedN < openedN:
                stack.append(")")
                genParen(closedN + 1, openedN)
                stack.pop()
        genParen(0, 0)
        return res

        