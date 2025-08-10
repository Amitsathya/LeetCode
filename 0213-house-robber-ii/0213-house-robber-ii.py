class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helperFunc(nums[1:]), self.helperFunc(nums[:-1]))

    def helperFunc(self, nums):
        first, second = 0, 0
        for i in range(len(nums)):
            temp = max(first + nums[i], second)
            first = second
            second = temp
        return second