class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(close, openN):
            if close == openN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append('(')
                dfs(close, openN + 1)
                stack.pop()

            if close < openN:
                stack.append(')')
                dfs(close + 1, openN)
                stack.pop()
        dfs(0, 0)
        return res