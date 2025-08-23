class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helperRob(nums[1:]), self.helperRob(nums[:-1]))

    def helperRob(self, nums):
        first, second = 0, 0
        for n in nums:
            temp = max(second, first + n)
            first = second
            second = temp
        return second