class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = res
        for n in nums[1:]:
            total = max(n, total + n)
            res = max(res, total)
        return res