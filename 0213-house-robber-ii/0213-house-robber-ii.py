class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.helperRob(nums[:-1]), self.helperRob(nums[1:]), nums[0])

    def helperRob(self,nums):
        first, second = 0, 0
        for i in range(len(nums)):
            temp = max(second + nums[i], first)
            second = first
            first = temp
        return first