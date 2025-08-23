class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        max_sumArr = nums[0]

        for i in range(1, len(nums)):
            max_sumArr = max(nums[i], nums[i] + max_sumArr)
            res = max(res, max_sumArr)
        return res