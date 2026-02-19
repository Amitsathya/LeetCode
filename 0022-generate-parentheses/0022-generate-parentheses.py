class Solution:
    def generateParenthesis(self, n):
        res = []
        def dfs(openParen, closeParen, temp):
            if closeParen == n == openParen:
                temp = "".join(temp)
                res.append(temp)
                return
            if openParen < n:
                temp.append("(")
                dfs(openParen + 1, closeParen, temp)
                temp.pop()
            
            if closeParen < openParen:
                temp.append(")")
                dfs(openParen, closeParen + 1, temp)
                temp.pop()
        dfs(0, 0, [])
        return res
