class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x%10 == 0 ):
            return False

        half_reverse = 0

        while x > half_reverse:
            half_reverse = half_reverse*10 + x%10
            x //= 10
        return half_reverse == x or half_reverse//10 == x


        