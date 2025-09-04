class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in rem:
                return [i, rem[diff]]
            rem[v] = i