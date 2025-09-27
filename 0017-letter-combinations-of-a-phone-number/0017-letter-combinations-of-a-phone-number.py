class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitsToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backTrack(i, curr):
            if i == len(digits):
                res.append(curr)
                return
            for c in digitsToChar[digits[i]]:
                backTrack(i + 1, curr + c)
        if digits:
            backTrack(0, "")
        return res