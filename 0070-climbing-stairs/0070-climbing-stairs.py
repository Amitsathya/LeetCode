class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1
        while n:
            temp = first + second
            second = first
            first = temp
            n -= 1
        return second