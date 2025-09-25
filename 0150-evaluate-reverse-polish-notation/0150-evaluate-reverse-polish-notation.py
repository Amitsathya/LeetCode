class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for c in tokens:
            if c == '+':
                res.append(res.pop() + res.pop())
            elif c == '*':
                res.append(res.pop() * res.pop())
            elif c == '-':
                v1, v2 = res.pop(), res.pop()
                res.append(v2 - v1)
            elif c == '/':
                v1, v2 = res.pop(), res.pop()
                res.append(int(v2/v1))
            else:
                res.append(int(c))
        return res[0]