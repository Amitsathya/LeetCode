class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxSum = res
        for n in nums[1:]:
            maxSum = max(n, n + maxSum)
            res = max(res, maxSum)
        return res