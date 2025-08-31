class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0
        for n in nums:
            temp = max(n + first, second)
            first = second
            second = temp
        return second