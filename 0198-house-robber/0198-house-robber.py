class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0
        for n in nums:
            temp = max(second, first + n)
            first = second
            second = temp
        return second