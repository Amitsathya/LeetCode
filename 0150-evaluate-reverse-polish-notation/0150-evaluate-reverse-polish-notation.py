class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for c in tokens:
            if c not in '/*+-':
                res.append(int(c))
            else:
                val1 = res.pop()
                val2 = res.pop()
                match c:
                    case '*':
                        res.append(val2 * val1)
                    case '+':
                        res.append(val2 + val1)
                    case '-':
                        res.append(val2 - val1)
                    case '/':
                        res.append(int(val2 / val1))
        return res[-1]