class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LENS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    LENS[i] = max(LENS[i], 1 + LENS[j])
        return max(LENS)