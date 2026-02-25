class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        while x!=0:
            digit = x % 10

            if x < 0 and digit > 0:
                digit -= 10

            x = (x-digit) // 10
            # x = x//10
            if res > 214748364 or (res == 214748364 and digit > 7):
                return 0
            if res < -214748364 or (res == -214748364 and digit <-8):
                return 0
            
            res = res * 10 + digit
        return res 
