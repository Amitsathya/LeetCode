class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for c in tokens:
            if c == '+':
                res.append(res.pop() + res.pop())
            elif c == '*':
                res.append(res.pop() * res.pop())
            elif c == '-':
                val1, val2 = res.pop(), res.pop()
                res.append(val2 - val1)
            elif c == '/':
                val1, val2 = res.pop(), res.pop()
                res.append(int(val2 / val1))
            else:
                res.append(int(c))
        return res[0]
