class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LEN = [1] * len(nums)
        for i in range(len(nums), -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    LEN[i] = max(LEN[i], 1 + LEN[j])
        return max(LEN)