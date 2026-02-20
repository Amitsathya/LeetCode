class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitsToChar = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def backTrack(i, temp):
            if i == len(digits):
                res.append("".join(temp))
                return
            for c in digitsToChar[digits[i]]:
                temp.append(c)
                backTrack(i + 1, temp)
                temp.pop()
        backTrack(0,[])
        return res