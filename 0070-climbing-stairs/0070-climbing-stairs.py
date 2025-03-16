class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1
        for i in range(n):
            temp = first + second
            second = first
            first = temp
        return second
        