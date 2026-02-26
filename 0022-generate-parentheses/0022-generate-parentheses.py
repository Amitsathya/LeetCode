class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, subset = [], []
        def dfs(closed, opened):
            if closed == n and opened == n:
                res.append("".join(subset))
                return
            
            if opened < n:
                subset.append('(')
                dfs(closed, opened + 1)
                subset.pop()

            if closed < opened:
                subset.append(')')
                dfs(closed + 1, opened)
                subset.pop()
        dfs(0, 0)
        return res