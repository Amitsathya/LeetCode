class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        sumSubarr= nums[0]
        for n in nums[1:]:
            res = max(res + n, n)
            sumSubarr = max(sumSubarr, res)
        return sumSubarr