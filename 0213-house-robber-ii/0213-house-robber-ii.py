class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helperFun(nums[1:]), self.helperFun(nums[:-1]))
    
    def helperFun(self, nums):
        first, second = 0, 0
        for n in nums:
            temp = max(first + n, second)
            first = second
            second = temp
        return second